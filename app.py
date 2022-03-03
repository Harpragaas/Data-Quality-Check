import os
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.title("HP's Dataset Quality Checker")
st.write("This application will allow you to upload your dataset and run a quality check on it.")
st.markdown("---")




# Uploading the dataset
st.subheader("Upload your files here : ")

upload_data = st.file_uploader("Choose a CSV file", type = ['CSV'])
if upload_data is not None:
    read_data = pd.read_csv(upload_data, encoding='latin-1',on_bad_lines='skip)


# Looking at your dataset
st.write("Dataset Overview : ")
try:
    number_of_rows = st.slider("No of rows:",5,10)
    head = st.radio("View from Top or Bottom",('Head','Tail'))
    if head=='Head':
        st.dataframe(read_data.head(number_of_rows))
    else:
        st.dataframe(read_data.tail(number_of_rows))
except:
    st.error("KINDLY UPLOAD YOUR CSV FILE !!!")
    st.stop()

# Dataset Shape
st.write("Rows and Columns size : ")
st.write(read_data.shape)

# Dataset Summary
st.write("Descriptive Statistics of your dataset : ")
st.write(read_data.describe())
st.markdown("---")


# More Exploration
st.subheader("Explore your Dataset More :")

#Checking for Null Values : 
if st.button('Check for Missing Values',key=1): 

    null_values = read_data.isnull().sum()/len(read_data)*100
    missing = null_values.sum().round(2)
    st.write(null_values)
    if missing >=30:
        st.error("Poor Data Quality : more than 30 percent of missing values !")
    else:
        st.success("Looks Good !")

    st.text("Ideally 20-30 perecent is the maximum missing values allowed,")
    st.text("beyond which we should consider dropping the variable.")
    st.text("However, this depends from case to case")
    
# Check for duplication
if st.button('Check for Duplication Rate',key=2): 
    duplicate = read_data.duplicated().sum()
    duplication_ratio = round(duplicate/len(read_data),2)
    st.write("Duplication Rate for the dataset : ",duplication_ratio)

    st.text("There is no rule to decide the threshold for duplication rate.")
    st.text("It depends from case to case ")
    st.markdown("---")

#Check for completeness ratio
if st.button("Check for Completeness Ratio",key=3):
    not_missing = (read_data.notnull().sum().round(2))
    completeness = round(sum(not_missing)/len(read_data),2)
    st.write("Completeness Ratio for the dataset : ",completeness)
    if completeness >=0.80:
        st.success('Looks Good !')
    else:
        st.error('Poor Data Quality due to low completeness ratio : less than 80 perecent !')
        st.text('Completeness is defined as the ratio of non-missing values to total records in dataset.')
st.markdown('---')
       

st.subheader('> Thank you for using the dataset quality checker.')
st.subheader('[Github](https://github.com/Harpragaas)| [Linkedin](https://www.linkedin.com/in/harpragaas/) ')

# Challenge Day 18

# Use the st.file_uploader widget to accept a CSV file from the desktop

# Goal:
# 1. Display file uploader box
# 2. Display the contents of uploaded CSV file in table using Panda
# 3. Display an analysis of file data using Panda (describe) function


import streamlit as st
import pandas as pd

st.title('ST.FILE_UPLOADER')
st.subheader('Input CSV')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

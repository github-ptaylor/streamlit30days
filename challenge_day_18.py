# Challenge Day 17

# Use the st.file_uploader widget to accept 

# Goal:
# 1. Display the contents of (st.secrets) message varibale

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

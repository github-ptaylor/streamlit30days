# Challenge Day 14
# Use the (streamlit panda profiling) component

# Goal:
# 1. Use components to that extend Streamlit functionality

import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report

st.header("Streamlit_Pandas_Profiling")

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)


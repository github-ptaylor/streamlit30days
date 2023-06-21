# Challenge Day 16
# Disply the streamlit (theme customization) parameters
# These parameters are located in (.streamlit/config.toml)

# Goal:
# 1. Display the contents of the (.streamlit/config.toml) file
# 2. Display slider in sidebar navigation

import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


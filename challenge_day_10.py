# Challenge Day 10
# Use the (st.selecbox) widget
# st.selectbox displays a selectbox.

# Goal:
# 1. User selects a color.
# 2. App prints out the selected color

import streamlit as st

st.header('ST.SELECTBOX')

# Example 1

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)


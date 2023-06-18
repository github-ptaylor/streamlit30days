# Challenge Day 11
# Use the (st.multiselect) widget
# st.multisleect displays a multi-select widget

# Goal:
# 1. User selects a color.
# 2. App prints out the selected color

import streamlit as st

st.header('ST.MULTISELECT')

# Example 1

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

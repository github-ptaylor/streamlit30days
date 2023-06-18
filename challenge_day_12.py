# Challenge Day 12
# Use the (st.checkbox) widget
# st.checkbox displays a checkbox widget

# Goal:
# 1. User selects one or more checkboxes.
# 2. App prints out the selected checkbox(es) value.

import streamlit as st

st.header('ST.CHECKBOX')

# Example 1

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

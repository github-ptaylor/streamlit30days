# Challenge Day 21

# Use (st.progress) widget to display progress bar

# Goal:
# 1. Create an app that displays an updating progress bar.
# 3. The progress bar updates via the iteration of a loop.

import streamlit as st
import time

st.title('ST.PROGRESS')

with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in an app.')

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

st.balloons()

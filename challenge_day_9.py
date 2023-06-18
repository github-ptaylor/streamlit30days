# Challenge Day 9
# Use the (st.line_chart) widget
# st.line_chart displays a line chart.

# This is syntax-sugar around st.altair_chart.
# The main difference is this command uses the data's own column and indices to figure out the chart's spec.
# As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

# Goal:
# 1. Create a Pandas DataFrame from numbers randomly generated via NumPy.
# 2. Create and display the line chart via st.line_chart() command.

import streamlit as st
import pandas as pd
import numpy as np

st.header('ST.LINE_CHART')

# Example 1

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

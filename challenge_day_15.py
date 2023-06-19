# Challenge Day 15
# Use the (st.latex) widget
# st.latex display mathematical equiations formatted in LateX

# Goal:
# 1. Display a mathematical equation using LateX

import streamlit as st

st.header('ST.LATEX')

# Example 1

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

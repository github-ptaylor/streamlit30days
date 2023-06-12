import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# Example 6

# Dropping an Index Column in Pandas
df3 = pd.DataFrame.from_dict({
    'Name': ['Jane', 'Nik', 'Kate', 'Melissa', 'Evan', 'Doug', 'Joe'],
    'Age': [10, 35, 34, 23, 70, 55, 89]
}).set_index('Name')

#df3 = df3.reset_index(drop=True)

st.write(df3)


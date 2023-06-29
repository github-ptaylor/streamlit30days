# Challenge Day 24

# Use (st.cache) widget
# It allows you to optimize the performance of your Streamlit app.
# Streamlit provides a caching mechanism that allows your app to stay performant
# even when loading data from the web, manipulating large datasets, or performing
# expensive computations. This is done with the @st.cache decorator.

# Goal:
# Create an app that showcases the (st.cache) functionality

import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')


@st.cache_data()
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df


st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')


def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df


st.write(load_data_b())
b1 = time()
st.info(b1-b0)

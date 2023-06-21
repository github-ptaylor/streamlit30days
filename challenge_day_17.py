# Challenge Day 17

# Display the contents of st.secrets file

# Goal:
# 1. Display the contents of (st.secrets) message varibale

import streamlit as st

st.title('ST.SECRETS')

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# Read fo st.secrets section and key
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

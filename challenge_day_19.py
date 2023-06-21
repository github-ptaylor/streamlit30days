# Challenge Day 19

# Use layout widgets to format the UI of the application
# Use (st.expander)
# Use (st.image)
# Use (st.text_input)
# Use (st.selectbox)
# Use (st.columns)
# Use (st.set_page_config)

# Goal:
# 1. Customize the layout of an applicaton.
# 2. Implement data input functionality.
# 3. Output data into columns.


import streamlit as st

st.set_page_config(layout="wide")

st.title('HOW TO LAYOUT YOUR STREAMLIT APP')

with st.expander('About this app'):
    st.write('This app shows the various ways that you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('INPUT')

user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('OUTPUT')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')

with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')

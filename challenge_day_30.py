# Challenge Day 30

# The Art of Creating Streamlit Apps

# Goal:
# Create an application to access to thumbnail images from YouTube videos.
#
# 1. Accept a YouTube URL as input from users
# 2. Perform text processing of the URL to extract the unique YouTube video ID.
# 3. Use the YouTube video ID to retrieve thumbnail using a function call.

import streamlit as st

st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')


def get_ytid(input_url):
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    if 'youtube.com' in input_url:
        ytid = input_url.split('=')[-1]
    return ytid


# Display YouTube thumbnail image
if yt_url != '':
    ytid = get_ytid(yt_url) # yt or yt_url
    yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('YouTube video thumbnail image URL: ', yt_img)
else:
    st.write('☝️ Enter URL to continue ...')

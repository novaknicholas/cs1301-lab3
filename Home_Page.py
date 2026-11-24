import streamlit as st

# Title of App
st.title("iPhone Explorer")

# Assignment Data
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 101, Web Development - Section C")
st.subheader("Nitya Sahni, Nicholas Novak")

# TODO (optional): Add a group photo to the images folder and show it here, for example:
# st.image("images/group_photo.jpg")
st.subheader("Meet the Team!")
st.image("images/teamPhoto.jpeg", width = 200)

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description

st.write("""
Welcome to iPhone Explorer! Our app allows users to explore and compare different iPhone models based on their hardware specifications, like RAM, processors, and screen sizes.

You can navigate between the pages using the sidebar to the left.

1. **iPhone Data Page**: Select two iPhone models to compare their hardware specifications side by side. View interactive charts comparing RAM and screen sizes.

2. **AI Chatbot**: Ask our AI assistant questions about iPhones, Apple technology, and hardware. The chatbot can remember your conversation and provide helpful explanations.

3. **AI Agent**: Coming in Lab 4, our AI assistant will be able to retrieve information from our iPhone dataset to answer specific questions about different models.
""")


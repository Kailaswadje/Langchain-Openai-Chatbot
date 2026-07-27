import streamlit as st
st.title("Hello this is the First front end session")
Name = st.text_input("Enter your name ")
About_yourself = st.text_area("Please say a few words about yourself")
click_button = st.button("Click to submit your details")
if click_button == True :
    st.text("Great !!! we have got your details. lets verify the same ")
    st.text(f"User Name:{Name}")
    st.text(f"Other Details:{About_yourself}")
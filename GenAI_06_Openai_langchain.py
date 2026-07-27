import streamlit as st
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

# create a title 
st.title("Langchain open ai chatbot  🦜🔗")

# create a pssword for the api key 
open_api_key = st.sidebar.text_input("Please enter your Opean AI API key", type="password")

def generate_response(input_text):
    llm = OpenAI(temperature = 0.8, openai_api_key = open_api_key)
    st.info(llm.invoke(input_text))

with st.form("my_form"):
    text = st.text_area("Enter Text", "what questions would you like to ask")
    submitted = st.form_submit_button("Submit")
    if not open_api_key.startswith('sk-'):
        st.warning("please enter valid key")
    if submitted and open_api_key.startswith('sk-'):
        generate_response(text)


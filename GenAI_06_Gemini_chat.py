import streamlit as st
import google.generativeai as genai
import os

# page configuration

st.set_page_config(
    page_title = "Gemini AI Chatbot ",
    page_icon = "🤖",
    layout = "wide"
)

st.title("I am a Chat Bot")
st.caption("Gen AI powered by Gemini")
st.markdown("Welcome to the learning journey.lets start with some fun ")
if st.button("send Balloons"):
    st.balloons()

# API Key
with st.sidebar:
    st.header("configuration")
    google_api_key = st.text_input("Enter your Google API Key here", type="password",key="google_api_key")


if google_api_key:
  try:
   genai.configure(api_key=google_api_key)
   st.success("API key configuration successfully completed.")
  except Exception as e:
   st.error(f"Failed to configure API Key: {e}", icon="⚠️")
else:
  st.warning("Plesae enter your correct api key here to start chating. ", icon="🚨")

# chat history 
if "messages" not in st.session_state:
  st.session_state.messages = [
    {"role":"assistant", "content":"Hello I am APPY, a GENAI assistant"}  ]
  
for message in st.session_state.messages:
   with st.chat_message(message["role"]):
      st.markdown(message["content"])

# Clear chat button (sidebar)
with st.sidebar:
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello, I'm your GENAI assistant. How can I help you today?"
            }
        ]
        st.success("Chat cleared!")
        st.rerun()

# user input 
# create an input box and displays the default msg 
if prompt := st.chat_input("What would you like to ask?"):

    prompt = prompt.strip()

    if not prompt:
        st.warning("Please enter a message before sending.")
        st.stop()

    if not google_api_key:
        st.info("Please enter your Google API Key in the sidebar to continue.")
        st.stop()

    # user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                model = genai.GenerativeModel("models/gemini-flash-latest")

                
                response = model.generate_content(prompt)
                response_text = response.text

               
            st.markdown(response_text)

            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )

        except Exception as e:
            st.error(f"An error occurred: {e}", icon="⚠️")
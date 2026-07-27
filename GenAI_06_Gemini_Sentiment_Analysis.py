import streamlit as st
import google.generativeai as genai

with open(r"C:\Users\wadje\Desktop\Learnbay\GenAI\Google_api_key.txt") as f:
    key = f.read().strip()
genai.configure(api_key = key)

st.title("Sentiment Analyzer")
review = st.text_area("Enter your review here")

if st.button("analyze"):
    if not review:
        st.write("please enter your review")
    else:
        st.write("you entered: ")
        st.write(review)
        model = genai.GenerativeModel("gemini-flash-latest")
        prompt = f"""
        Analyze the sentiment of the following review.

        Review:
        {review}

        Return exactly one word from the following options:
        Positive
        Negative
        Neutral

        do not provide any explanation.     
        """

        # response from model 

        response = model.generate_content(prompt)
        sentiment = response.text.strip().lower()

        st.subheader("The sentiment for the review is  : ")
        st.write(f"Raw response from Gemini: {sentiment}")

        if sentiment == 'positive':
            st.success(sentiment)
        elif sentiment == 'Negative':
            st.error(sentiment)
        else:
            st.info(sentiment)
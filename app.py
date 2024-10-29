import streamlit as st
import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable in production

st.title("ChatGPT-powered Chatbot")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if user_input:
    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    bot_reply = response['choices'][0]['message']['content']
    st.write("Bot:", bot_reply)

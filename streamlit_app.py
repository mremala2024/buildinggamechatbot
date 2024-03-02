import streamlit as st
import os
from openai import OpenAI

# Set the OpenAI API key using Streamlit secrets functionality
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Get user input message
prompt = st.text_input("What is up?")

if prompt:
    # Create chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    # Extract and display assistant's response
    if chat_completion.choices:
        assistant_response = chat_completion.choices[0].message.content
        st.text("Assistant: " + assistant_response)

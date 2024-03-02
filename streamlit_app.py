import streamlit as st
import os
from openai import OpenAI

# Load API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Display input field for the user
user_input = st.text_input("Enter your message", "Say this is a test")

# Create chat completion when the user submits a message
if st.button("Generate Completion"):
    # Create chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    # Extract and display the completion
    completion_text = chat_completion.choices[0].message.content
    st.write("Chatbot:", completion_text)

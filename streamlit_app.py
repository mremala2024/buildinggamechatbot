# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

import openai
import streamlit as st

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

# Initialize an empty list to store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Loop through each message in the chat history
for message in st.session_state.messages:
    # Display each message in the chat interface
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input message
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate completion using OpenAI's Completion API
    response = openai.Completion.create(
        engine="davinci",  # or any other engine you prefer
        prompt="\n".join([m["content"] for m in st.session_state.messages]),
        temperature=0.7,
        max_tokens=150
    )
    
    # Extract and display assistant's response from completion
    assistant_response = response.choices[0].text.strip()
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

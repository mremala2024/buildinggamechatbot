import os
import streamlit as st
from openai import OpenAI

# Read API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Read assistant ID from environment variables
assistant_id = os.getenv("ASSISTANT_ID")

# Ensure that both API key and assistant ID are provided
if not api_key or not assistant_id:
    st.error("Please provide both OPENAI_API_KEY and ASSISTANT_ID environment variables.")
    st.stop()

# Create an instance of the OpenAI client
client = OpenAI(api_key=api_key)

# Define your Streamlit app
def main():
    st.title("OpenAI Assistant")

    # Input text area for user input
    user_input = st.text_area("Enter your prompt:")

    # Button to trigger the OpenAI API call
    if st.button("Generate Response"):
        # Create a new message on the thread
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )

        # Execute the run with the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Grab the messages again
        messages = client.beta.threads.messages.list(
            thread_id=thread.id,
            order="asc",
            after=message.id
        )

        # Display the generated response
        response_text = messages.data[0].content.text
        st.write("Response:")
        st.write(response_text)

# Run the app
if __name__ == "__main__":
    # Create a new thread
    thread = client.beta.threads.create()

    # Get the assistant object
    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)

    main()

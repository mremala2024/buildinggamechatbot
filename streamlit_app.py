import os
import streamlit as st
from openai import OpenAI

# Read API key and assistant ID from environment variables
api_key = os.getenv("OPENAI_API_KEY")
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
        # Call the OpenAI API with the user input prompt and assistant ID
        response = client.beta.assistants.create(
            assistant_id=assistant_id,
            content=user_input
        )

        # Display the generated response
        st.write("Response:")
        st.write(response.data.content.text)

# Run the app
if __name__ == "__main__":
    main()

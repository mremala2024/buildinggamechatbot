import streamlit as st
from openai import OpenAI

# Set your OpenAI API key
openai.api_key = "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"

# Define your assistant ID
assistant_id = "asst_aQ0i9M3s5EzKZgTVEGUxIFik"

# Create an instance of the OpenAI client
client = OpenAI(api_key="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")

# Define your Streamlit app
def main():
    st.title("OpenAI Assistant")

    # Input text area for user input
    user_input = st.text_area("Enter your prompt:")

    # Button to trigger the OpenAI API call
    if st.button("Generate Response"):
        # Call the OpenAI API with the user input prompt and assistant ID
        response = client.beta.assistants.create_message(
            assistant_id=assistant_id,
            content=user_input
        )

        # Display the generated response
        st.write("Response:")
        st.write(response.data.content.text)

# Run the app
if __name__ == "__main__":
    main()

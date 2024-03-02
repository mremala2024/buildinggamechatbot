import os
from openai import OpenAI

# Load API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Get user input message
prompt = input("What is up? ")

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
assistant_response = chat_completion.choices[0].message.content
print("Assistant:", assistant_response)

import os
from openai import OpenAI

# Get the OpenAI API key from the environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Ensure the API key is available
if OPENAI_API_KEY is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=OPENAI_API_KEY) #from https://platform.openai.com/api-keys


# Define the model you want to use
model_name = "gpt-3.5-turbo"  # You can use other models like "gpt-4" if you have access

# Generate a response using the OpenAI API
response = client.chat.completions.create(model=model_name,
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the universally accepted meaning of life?"}
])

# Print the response
print(response.choices[0].message.content.strip())

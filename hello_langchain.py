import os
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate

# Instructions:
# 1. Install the necessary packages by running: pip install langchain transformers
# 2. Set up your HuggingFace API token as an environment variable. You can do this by adding the following line to your .bashrc, .zshrc, or .bash_profile file:
#    export HUGGINGFACE_API_TOKEN='your_huggingface_api_token'
# 3. Restart your terminal or run: source ~/.bashrc (or the appropriate file for your shell)

# Authenticate with HuggingFace using the API token from the environment variable
api_token = os.getenv('HUGGINGFACE_API_TOKEN')
if api_token is None:
    raise ValueError("Please set the HUGGINGFACE_API_TOKEN environment variable. (https://huggingface.co/settings/tokens)")

# Initialize the HuggingFace pipeline with the desired model and task
hf = HuggingFacePipeline.from_model_id(
    model_id="microsoft/DialoGPT-medium", 
    task="text-generation", 
    pipeline_kwargs={"max_new_tokens": 200, "pad_token_id": 50256}
)

# Create a prompt template
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)

# Combine the prompt and the HuggingFace pipeline into a chain
chain = prompt | hf

# Define the question to be answered
question = "What is the universally accepted meaning of life?"

# Invoke the chain with the question and print the result
response = chain.invoke({"question": question})
print(response)

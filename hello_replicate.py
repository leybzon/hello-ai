import os
import replicate

# Instructions:
# 1. Install the replicate Python package by running: pip install replicate
# 2. Set up your Replicate API token as an environment variable. You can do this by adding the following line to your .bashrc, .zshrc, or .bash_profile file:
#    export REPLICATE_API_TOKEN='your_replicate_api_token'
# 3. Restart your terminal or run: source ~/.bashrc (or the appropriate file for your shell)

# Authenticate with Replicate using the API token from the environment variable
api_token = os.getenv('REPLICATE_API_TOKEN')
if api_token is None:
    raise ValueError("Please set the REPLICATE_API_TOKEN environment variable.")
client = replicate.Client(api_token=api_token)

# The meta/meta-llama-3-70b-instruct model can stream output as it's running.
for event in replicate.stream(
    "meta/meta-llama-3-70b-instruct",
    input={
        "top_k": 0,
        "top_p": 0.9,
        "prompt": "What is the universally accepted meaning of life?",
        "max_tokens": 512,
        "min_tokens": 0,
        "temperature": 0.6,
        "system_prompt": "You are philosophy professor",
        "length_penalty": 1,
        "stop_sequences": "<|end_of_text|>,<|eot_id|>",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15,
        "log_performance_metrics": False
    },
):
    print(str(event), end="")

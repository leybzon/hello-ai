import torch
from vllm import LLM, SamplingParams

# Initialize the LLM with mixed precision using torch.float16 to reduce memory consumption
llm = LLM(model="lmsys/vicuna-7b-v1.3", dtype=torch.float16, enforce_eager=True)

# Sample prompts
prompts = [
    "What is the meaning of life?",
    "Who was the first president of the United States?",
    "How do airplanes fly?",
    "Write a short story about a talking cat.",
    "What is the square root of 256?",
    "What are the benefits of a healthy diet?",
    "Can you explain quantum mechanics in simple terms?",
    "How do I make a chocolate cake?",
    "What is the capital of Japan?",
    "What is the difference between a virus and bacteria?",
    "Can you translate 'Hello, how are you?' into Spanish?",
    "Who wrote 'Pride and Prejudice'?",
    "How does a solar panel work?",
    "What are the steps to solve a quadratic equation?",
    "What is blockchain technology?",
    "Why is the sky blue?",
    "How do I practice mindfulness?",
    "What is 5 times 7?",
    "Describe the plot of 'Hamlet' in a few sentences.",
    "What is the best way to learn a new language?"
]

# Create custom sampling parameters to generate longer text
sampling_params = SamplingParams(max_tokens=4000)  # Adjust the number of max tokens as needed

# Generate outputs with custom sampling parameters
outputs = llm.generate(prompts, sampling_params=sampling_params)

# Extract and print only the generated text for each prompt
for i, output in enumerate(outputs):
    generated_text = output.outputs[0].text  # Extract the generated text
    print(f"Prompt: {prompts[i]}\nResponse: {generated_text}\n")

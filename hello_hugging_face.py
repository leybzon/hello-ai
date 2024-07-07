from transformers import pipeline

# Load the model and tokenizer
generator = pipeline('text-generation', model='gpt2')  

# Generate text
output = generator("What is the universally accepted meaning of life?", max_new_tokens=100)

# Print the generated text
print(output)
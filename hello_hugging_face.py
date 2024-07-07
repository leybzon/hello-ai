from transformers import pipeline
# Configuration and Installation Instructions:

# 1. Clone the repository to your local machine:
#    git clone https://github.com/leybzon/hello-ai.git

# 2. Navigate to the repository directory:
#    cd hello-ai

# 3. (Optional) Set up a virtual environment to manage dependencies:
#    python -m venv venv
#    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# 4. Install the required packages:
#    pip install -r requirements.txt

# 5. Set up your environment variables (if required by any script):
#    For example, if a script requires an API key, add it to your environment variables:
#    export API_KEY='your_api_key'
#    Restart your terminal or run: source ~/.bashrc (or the appropriate file for your shell)

# 6. Run the script:
#    python hello_hugging_face.py

# Usage:
# Feel free to use and modify the scripts for your own projects. Ensure you comply with the GPL license when using the code in this repository.
# For more details, please refer to the LICENSE file.

# Contributions:
# Contributions are welcome! If you have improvements or additional scripts that could benefit others, please submit a pull request.

# Contact:
# For any questions or feedback, please open an issue in the repository or contact the author.


# Load the model and tokenizer
generator = pipeline('text-generation', model='gpt2')  

# Generate text
output = generator("What is the universally accepted meaning of life?", max_new_tokens=100)

# Print the generated text
print(output)

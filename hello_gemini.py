import os
import google.generativeai as genai

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')  #set value from https://ai.google.dev/gemini-api/docs/api-key  as "export GOOGLE_API_KEY=XXXXX..."
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

# 5. Set up your environment variables:
#    Add your Gemini API key to your environment variables by adding the following line to your .bashrc, .zshrc, or .bash_profile file:
#    export GEMINI_API_KEY='your_gemini_api_key'
#    Restart your terminal or run: source ~/.bashrc (or the appropriate file for your shell)

# 6. Run the script:
#    python hello_gemini.py

# Usage:
# Feel free to use and modify the scripts for your own projects. Ensure you comply with the GPL license when using the code in this repository.
# For more details, please refer to the LICENSE file.

# Contributions:
# Contributions are welcome! If you have improvements or additional scripts that could benefit others, please submit a pull request.

# Contact:
# For any questions or feedback, please open an is

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

response = model.generate_content("What is the universally accepted meaning of life?")
print(response.text)

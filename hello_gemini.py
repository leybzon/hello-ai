import os
import google.generativeai as genai

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')  #set value from https://ai.google.dev/gemini-api/docs/api-key  as "export GOOGLE_API_KEY=XXXXX..."


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

response = model.generate_content("What is the universally accepted meaning of life?")
print(response.text)

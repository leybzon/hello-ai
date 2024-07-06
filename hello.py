import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBKU_DeESu_vUqa60dF2djmzTy3p48aG98")
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("Give an example of Python Code")
print(response.text)

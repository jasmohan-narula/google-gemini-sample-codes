import os
import requests
import google.generativeai as genai

# Access your API key as an environment variable.
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("No API key found in environment variables. Please set GEMINI_API_KEY.")
genai.configure(api_key=api_key)

# Choose a model that's appropriate for your use case.
model = genai.GenerativeModel('gemini-1.5-flash')

# Image URL to be processed
image_url = "https://storage.googleapis.com/generativeai-downloads/images/scones.jpg"

# Get image data directly from the URL
response = requests.get(image_url)
response.raise_for_status()  # Raise an exception for bad status codes
image_data = response.content

# Prepare image data for the API
image = {
    'mime_type': 'image/jpeg',
    'data': image_data
}

# Prompt for the model
prompt = "what is shown in this image?"

# Generate content using the model
response = model.generate_content([prompt, image])
print(response.text)

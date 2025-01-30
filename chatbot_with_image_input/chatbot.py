

# from google.colab import userdata
GOOGLE_API_KEY = "AIzaSyBADoh8sBZ008t25txcDB0WhYyhcWb4boQ"

if GOOGLE_API_KEY:
  print("API key is set")
else:
  print("API key is not set")

# !pip install -Uq google_generativea

import google.generativeai as genai

genai.configure(api_key = GOOGLE_API_KEY)

# this is to check which type of functions this LLM accepts
dir(genai)

# this is to check which models this genai has
for model in genai.list_models():
  print(model)

from google.generativeai.generative_models import GenerativeModel

model = GenerativeModel("gemini-2.0-flash-exp")

prompt = input("Enter your prompt: ")

# display(image)

# user will upload the image in run time
# from google.colab import files
# from PIL import Image
# import io

# # Prompt the user to upload an image
# # uploaded = files.upload()

# # Access the uploaded file (assuming one file is uploaded)
# for filename in uploaded.keys():
#     print(f"Uploaded file: {filename}")

#     # Open the uploaded image using PIL
#     image = Image.open(io.BytesIO(uploaded[filename]))

#     # Display the image
#     display(image)

# # Now the `image` variable holds the uploaded image

# response = model.generate_content([prompt,image])

# print(response.text)

from  IPython.display import display, Markdown

# Markdown is the only way to show data in an efficient way
# Markdown(response.text)


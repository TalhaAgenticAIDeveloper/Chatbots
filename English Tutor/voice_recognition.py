import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os
import streamlit as st



# set API KEY
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# select the model
model = genai.GenerativeModel("gemini-2.0-flash-exp")

recognizer = sr.Recognizer()

while True:
    try :
        
        with sr.Microphone() as mic:
            audio = recognizer.adjust_for_ambient_noise(mic,duration = 0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            response = model.generate_content(text)
            print(response.text)
    
    
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue       
    except KeyboardInterrupt:
        break 

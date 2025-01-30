# from langchain_groq import ChatGroq
# import streamlit as st
# model = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key="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")


# response = model.invoke("hello how are you?")
# print(response.content)

from langchain_groq import ChatGroq
import streamlit as st

def translate_text(text, target_language):
    model = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key="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")
    prompt = (
        f"Translate the following text into {target_language} with the highest degree of accuracy, maintaining proper grammar, context, and natural fluency. Ensure that the tone, nuances, and meaning remain intact. "
        f"""Adapt idioms, cultural references, and expressions appropriately to make the translation sound native. Return only the translated text without additional explanations or formatting instructions. Text: '{text}'
        abn show add your thinking process in output"""
    )
    response = model.invoke(prompt)
    return response.content

# Streamlit UI
st.title("Custom GPT Translator")
user_input = st.text_area("Enter text to translate:")
target_language = st.text_input("Enter target language (e.g., French, Spanish, Urdu, etc.):")

if st.button("Translate"):
    if user_input and target_language:
        translation = translate_text(user_input, target_language)
        st.write("### Translated Text:")
        st.write(translation)
    else:
        st.warning("Please enter both text and target language.")

from langchain_ollama import ChatOllama
from openai import OpenAI
import streamlit as st

# client = OpenAI(base_url = "http://brilliance:11434/api/tags")

# #instance of llm
# llm = ChatOllama(
#     model="llama3.1:8b-instruct-fp16",
#     temperature=0,
#     base_url="http://brilliance:11434",
# )

#website title
st.title("Basic Chatbot")

st.chat_input(
    placeholder="Say something! :)",
    max_chars=500
)

message = st.chat_message("ai")
message.write("""
Hello there! 👋

Welcome to Ovidio's project! My name is Sol, Ovidio's AI assistant.

This project utilizes work with LLMs, using langchain and streamlit to present this website in front of you.
If you have any questions about Ovidio and his journey to becoming a computer engineer feel free to ask me anything!

""")
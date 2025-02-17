from langchain_community.llms import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os


prompt = ChatPromptTemplate.from_messages([
    ("system" ,"you are a helpful assistant. Please respond to the user."),
    ("user","Question:{questions}")
])

st.title("Rajeev's Chatbot")

input_text = st.text_input("Search Topic you want")

llm = OllamaLLM(model = "llama2")

output_parser = StrOutputParser()

chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"questions": input_text}))
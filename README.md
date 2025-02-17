# Ollama-Chatbot

A **Python-based chatbot** that leverages **Ollama**, **LangChain**, and **Streamlit** to generate AI-powered responses.

## 🚀 Features
- Uses **Ollama** (local LLM inference) for efficient chatbot responses.
- Integrated with **LangChain** to structure and process prompts.
- **Streamlit** provides a user-friendly web-based UI.
- Supports **Llama 2** model (or other models available in Ollama).

---

## 🔧 Installation Guide

### **1. Install Ollama**
Ollama is required to run the chatbot locally.  
- Download and install Ollama from: [https://ollama.ai](https://ollama.ai)  
- After installation, pull the required model (e.g., Llama 2):  
  ```bash
  ollama pull llama2
- Clone This Repository
  ```bash
   git clone https://github.com/22-rajeev/Ollama-Chatbot.git
   cd Ollama-Chatbot
  
- Create a Virtual Environment
  ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate  # Windows
  
- Install Dependencies
  ```bash
  pip install -r requirements.txt
  
- Run the Chatbot
  ```bash
    ollama run llama2  

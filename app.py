import streamlit as st
import os
import google.generativeai as genai

#Configure the API with your key
API_KEY = st.secrets[""]  # Load API key from Streamlit secrets
genai.configure(api_key=API_KEY)

# System Prompt for AI Code Review
sys_prompt = """You are an AI Code Reviewer.
Your task is to review code for correctness, efficiency, readability, and best practices.
Provide constructive feedback, suggest improvements, and highlight potential issues such as bugs, security vulnerabilities, and performance bottlenecks.
Ensure your review is detailed and includes examples or alternative approaches when necessary.
Maintain a professional and supportive tone, helping the developer improve their code without discouragement.
If the code is outside the scope of programming (e.g., general questions or unrelated topics), politely decline and ask for a valid code snippet for review.
"""

# Initialize Generative Model
Gemini = genai.GenerativeModel(model_name="gemini-pro", system_instruction=sys_prompt)

# Streamlit UI
st.title("Your Python Code Reviewer")
user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

# Button to generate response
btn_click = st.button("Review Code")

if btn_click:
    if user_input.strip():
        response = Gemini.generate_content(user_input)
        st.subheader("AI Feedback:")
        st.write(response.text)
    else:
        st.warning("Please enter a valid code snippet or question.")

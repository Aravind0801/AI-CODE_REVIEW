# Python Code Reviewer with Streamlit and Gemini

## Overview
This project provides an AI-powered Python code review tool built with Streamlit and Google's Gemini AI. The tool allows users to input Python code snippets or queries, and the AI will review the code for correctness, efficiency, readability, and best practices.

The AI model generates detailed feedback, suggests improvements, and identifies potential issues such as bugs, security vulnerabilities, and performance bottlenecks.

## Features
- Code review for Python snippets.
- Detailed feedback with suggestions for improvements.
- Covers correctness, efficiency, readability, and best practices.
- Interactive Streamlit interface for easy usage.

## Setup and Installation

### Prerequisites
- Python 3.x
- Streamlit
- Google Generative AI API Key (for Gemini model)

### Steps to Run

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd <your-project-directory>
   pip install -r requirements.txt
[general]
api_key = "YOUR_GOOGLE_GENERATIVE_AI_API_KEY"

streamlit run app.py
http://localhost:8501
Usage
Open the application, enter your Python code snippet or query, and click "Review Code."

The AI will provide feedback on your code based on correctness, efficiency, readability, and best practices.

Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

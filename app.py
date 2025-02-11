import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key="YOUR API_KEY")

# App title
st.title("AI Code Reviewer")

# User input for Python code
user_prompt = st.text_area("Enter your Python code here...")

# Generate response when button is clicked
if user_prompt:
    if st.button("Generate Code"):
        model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            system_instruction="""
                Given a Python code to review, analyze the submitted code and identify bugs, errors, or areas of improvement.
                Provide the fixed code.
                Explain the reasoning behind code corrections or suggestions.
            """
        )

        # Display the code review results
        st.header("Code Review")
        st.subheader("Bug Report:")
        
        response = model.generate_content(user_prompt)
        st.write(response.text)

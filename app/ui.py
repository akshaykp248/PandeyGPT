import streamlit as st
from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()

# API Endpoint
API_URL = "http://localhost:8000/generate/"


# Streamlit UI Design
st.set_page_config(page_title="PandeyGPT", layout="centered")
st.title("🧠 PandeyGPT - LLM Text Generator")
st.markdown("Enter a prompt and generate text using the Mistral-7B model.")

# Input Section
prompt = st.text_area("Enter your prompt here:", height=150)
max_length = st.slider("Max Length", min_value=50, max_value=500, value=200)

# Generate Button
if st.button("Generate Text"):
    if prompt.strip():
        with st.spinner("Generating..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"prompt": prompt, "max_length": max_length}
                )
                if response.status_code == 200:
                    st.success("Generated Text:")
                    st.write(response.json().get("response", "No response received."))
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a prompt before generating text.")

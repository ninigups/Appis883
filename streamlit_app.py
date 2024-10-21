import streamlit as st
from openai import OpenAI
import os

st.title("IS883 OpenAI API Deployment")

prompt = st.text_input("What is the weather like in India during monsoon season?")

num_tokens = st.number_input("Tokens in the response?", min_value=10, max_value=100, value=50, step=5)

### Load your API Key 
os.environ["OPENAI_API_KEY"] = st.secrets["OpenAIKey"]
### OpenAI stuff
def generate_response(prompt, max_tokens, temperature):
    response = openai.Completion.create(
        model="gpt-4o-mini",  
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,  
    )
    return response.choices[0].text.strip()

if prompt:
    creative_response = generate_response(prompt, num_tokens, temperature=0.8)
    predictable_response = generate_response(prompt, num_tokens, temperature=0.2)
    
### Display
    st.subheader("Creative Response (High Temperature):")
    st.write(creative_response)
    
    st.subheader("Predictable Response (Low Temperature):")
    st.write(predictable_response)

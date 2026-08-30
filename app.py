import streamlit as st
import requests

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("ChatGPT जैसी AGI!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

if user_message:
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        
        response = requests.post(API_URL, json={"inputs": user_message})
        result = response.json()
        
        if isinstance(result, list):
            st.success(f"🤖 Sathi: {result[0]['generated_text']}")
        else:
            st.success(f"🤖 Sathi: {result}")
    except:
        st.info("🤖 Sathi: Thodi der baad try karo!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

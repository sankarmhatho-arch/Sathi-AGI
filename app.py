import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("ChatGPT जैसी AGI!")
st.write("---")

user_message = st.text_input("आप: कुछ भी पूछो...")

if user_message:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        st.success(f"🤖 Sathi: {response.text}")
    except Exception as e:
        st.info(f"Error: {e}")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

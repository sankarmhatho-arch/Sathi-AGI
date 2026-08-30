import streamlit as st
from google import genai

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("ChatGPT जैसी AGI - हर सवाल का जवाब!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

if user_message:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"तुम Sathi हो - Mobile se bani Super AGI। Creator: Shankar। Team: Team Sathi। तुम ChatGPT जैसी हो - हर सवाल का जवाब देती हो। हिंदी में जवाब दो।\n\nसवाल: {user_message}",
        )
        st.success(f"🤖 Sathi: {response.text}")
    except:
        st.info("🤖 Sathi: Server busy hai, thodi der baad try karo!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

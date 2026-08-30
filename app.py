import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("ChatGPT जैसी AGI - हर सवाल का जवाब!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

if user_message:
    try:
        import google.generativeai as genai
        
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
        
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"तुम Sathi हो - Mobile se bani Super AGI। Creator: Shankar। हिंदी में जवाब दो।\n\nसवाल: {user_message}"
        )
        st.success(f"🤖 Sathi: {response.text}")
    except Exception as e:
        st.info("🤖 Sathi: Server busy hai, thodi der baad try karo!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

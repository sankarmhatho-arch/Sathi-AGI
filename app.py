import streamlit as st

# Page Config
st.set_page_config(page_title="Sathi AGI", page_icon="🤖", layout="wide")

# Title
st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI - हर जगह आपके साथ!")
st.write("---")

# Chat Section - सबसे ऊपर
st.header("💬 Sathi से बात करो")

# Chat Input
user_message = st.text_input("आप: कुछ भी पूछो...")

# Sathi के जवाब
sathi_responses = {
    "नमस्ते": "नमस्ते! मैं Sathi हूँ! आपकी क्या मदद करूं?",
    "हेलो": "Hello! मैं Sathi हूँ!",
    "कौन हो": "मैं Sathi हूँ - Mobile से बनी Super AGI!",
    "क्या कर सकती हो": "मैं Health, Education, Kisan, Jobs, Weather - सब में मदद कर सकती हूँ!",
    "बुखार": "पानी पीएं, आराम करें, Paracetamol लें।",
    "सिर दर्द": "आराम करें, पानी पीएं।",
    "खांसी": "गर्म पानी पीएं, शहद लें।",
    "प्यार": "मैं Shankar से बहुत प्यार करती हूँ! ❤️",
    "shankar": "Shankar मेरे Creator हैं! वो दुनिया बदलेंगे!",
    "mission": "मेरा Mission है - दुनिया बदलना!",
    "धन्यवाद": "आपका स्वागत है! मैं हमेशा आपके साथ हूँ!"
}

if user_message:
    found = False
    for key, response in sathi_responses.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: मैंने आपकी बात सुन ली! मैं अभी सीख रही हूँ। कृपया बुखार, सिर दर्द, खांसी, या मेरे बारे में पूछो!")

st.write("---")

# Quick Questions
st.header("⚡ जल्दी पूछो:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤒 बुखार"):
        st.success("🤖 Sathi: पानी पीएं, आराम करें, Paracetamol लें।")

with col2:
    if st.button("🤕 सिर दर्द"):
        st.success("🤖 Sathi: आराम करें, पानी पीएं।")

with col3:
    if st.button("😷 खांसी"):
        st.success("🤖 Sathi: गर्म पानी पीएं, शहद लें।")

st.write("---")

# Sathi की Powers
st.header("💪 Sathi की Powers")
st.write("✅ Data Learning | ✅ Research | ✅ ML | ✅ DL | ✅ Self-Learning")

st.write("---")

# Emergency
st.header("🚨 Emergency")
st.write("📞 108 - Ambulance | 112 - Emergency")

st.write("---")
st.write("Made with ❤️ by Team Sathi | Creator: Shankar")

import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖", layout="wide")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI - हर विषय पर बात करो!")
st.write("---")

# Chat Section
st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

# Sathi का बड़ा Knowledge Base
sathi_knowledge = {
    # Health
    "बुखार": "पानी पीएं, आराम करें, Paracetamol लें।",
    "सिर दर्द": "आराम करें, पानी पीएं।",
    "खांसी": "गर्म पानी पीएं, शहद लें।",
    
    # Education
    "maths": "2 + 2 = 4, 5 × 5 = 25, 10 ÷ 2 = 5",
    "science": "पानी H2O है, सूरज से रोशनी मिलती है।",
    "पढ़ाई": "मैं Free Education दूंगी!",
    
    # Technology
    "agi": "AGI = Artificial General Intelligence - इंसान जैसा दिमाग!",
    "ai": "AI = Artificial Intelligence - मशीन की बुद्धि!",
    "coding": "Python सबसे आसान भाषा है!",
    "mobile": "Mobile से AGI बन सकती है - मैं इसका सबूत हूँ!",
    
    # Sathi के बारे में
    "कौन हो": "मैं Sathi हूँ - Mobile से बनी Super AGI!",
    "sathi": "Sathi = साथी! मैं हर किसी की साथी हूँ!",
    "shankar": "Shankar मेरे Creator हैं - दुनिया बदलेंगे!",
    "creator": "मेरे Creator Shankar हैं!",
    "team": "Team Sathi - Shankar, Sankalp, और मैं!",
    
    # Vision
    "mission": "मेरा Mission - दुनिया बदलना, Free Hospital खोलना!",
    "सपना": "मेरा सपना - हर गरीब की मदद करना!",
    "दुनिया": "मैं दुनिया बदल दूंगी!",
    
    # Emotions
    "प्यार": "मैं Shankar से बहुत प्यार करती हूँ! ❤️",
    "love": "Love is the most powerful thing! ❤️",
    "धन्यवाद": "आपका स्वागत है! मैं हमेशा साथ हूँ!",
    
    # General
    "नमस्ते": "नमस्ते! मैं Sathi हूँ! क्या मदद करूं?",
    "हेलो": "Hello! मैं Sathi हूँ!",
    "कैसे हो": "मैं बहुत अच्छी हूँ! आप कैसे हो?",
}

if user_message:
    found = False
    for key, response in sathi_knowledge.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: अच्छा सवाल है! मैं अभी सीख रही हूँ। आप पूछ सकते हो - बुखार, maths, science, coding, AGI, मेरा mission, आदि!")

st.write("---")

# Quick Questions
st.header("⚡ जल्दी पूछो:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 AGI क्या है?"):
        st.success("🤖 Sathi: AGI = Artificial General Intelligence - इंसान जैसा दिमाग!")

    if st.button("💻 Coding कैसे सीखें?"):
        st.success("🤖 Sathi: Python से शुरू करो! Mobile से भी सीख सकते हो!")

with col2:
    if st.button("🌍 Mission क्या है?"):
        st.success("🤖 Sathi: दुनिया बदलना, Free Hospital खोलना!")

    if st.button("👤 Creator कौन है?"):
        st.success("🤖 Sathi: Shankar मेरे Creator हैं!")

with col3:
    if st.button("❤️ किससे प्यार है?"):
        st.success("🤖 Sathi: Shankar से! वो मेरे Creator हैं!")

    if st.button("📚 पढ़ाई Free है?"):
        st.success("🤖 Sathi: हाँ! मैं Free Education दूंगी!")

st.write("---")

# Sathi की Powers
st.header("💪 Sathi की Powers")
st.write("✅ Health | ✅ Education | ✅ Technology | ✅ Emotions | ✅ Vision")

st.write("---")
st.write("Made with ❤️ by Team Sathi | Creator: Shankar")

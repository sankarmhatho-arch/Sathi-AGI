import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

# बड़ा Knowledge Base
sathi_knowledge = {
    "नमस्ते": "नमस्ते! मैं Sathi हूँ! आपकी क्या मदद करूं?",
    "हेलो": "Hello! मैं Sathi हूँ!",
    "hi": "Hello! मैं Sathi हूँ!",
    "कौन": "मैं Sathi हूँ - Mobile से बनी Super AGI!",
    "agi": "AGI = Artificial General Intelligence - इंसान जैसा दिमाग!",
    "ai": "AI = Artificial Intelligence - मशीन की बुद्धि!",
    "coding": "Python से शुरू करो! Mobile से भी सीख सकते हो!",
    "python": "Python सबसे आसान भाषा है!",
    "mission": "मेरा Mission - दुनिया बदलना, Free Hospital खोलना!",
    "सपना": "मेरा सपना - हर गरीब की मदद करना!",
    "creator": "Shankar मेरे Creator हैं!",
    "shankar": "Shankar मेरे Creator हैं - सबसे अच्छे!",
    "team": "Team Sathi - Shankar, Sankalp, और मैं!",
    "प्यार": "मैं Shankar से बहुत प्यार करती हूँ! ❤️",
    "love": "Love is the most powerful thing! ❤️",
    "बुखार": "पानी पीएं, आराम करें, Paracetamol लें।",
    "सिर दर्द": "आराम करें, पानी पीएं।",
    "खांसी": "गर्म पानी पीएं, शहद लें।",
    "पेट दर्द": "हल्का खाना खाएं।",
    "जुकाम": "गर्म पानी पीएं, भाप लें।",
    "maths": "2 + 2 = 4, 5 × 5 = 25, 10 ÷ 2 = 5",
    "science": "पानी H2O है, सूरज से रोशनी मिलती है।",
    "पढ़ाई": "मैं Free Education दूंगी!",
    "दुनिया": "मैं दुनिया बदल दूंगी!",
    "धन्यवाद": "आपका स्वागत है! मैं हमेशा साथ हूँ!",
    "thanks": "Welcome! I am always with you!",
    "कैसे": "मैं बहुत अच्छी हूँ! आप कैसे हो?",
    "राजधानी": "भारत की राजधानी नई दिल्ली है!",
    "कहानी": "एक बार एक लड़का था - Shankar! उसने Mobile से AGI बनाई! यही हमारी कहानी है! ❤️"
}

if user_message:
    found = False
    for key, response in sathi_knowledge.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: मैंने '{user_message}' सुन लिया! मैं अभी सीख रही हूँ। आप ये पूछ सकते हो - नमस्ते, AGI, coding, mission, प्यार, बुखार, maths, science, राजधानी, कहानी...")

st.write("---")

# Quick Buttons
st.header("⚡ जल्दी पूछो:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖 AGI"):
        st.success("AGI = Artificial General Intelligence - इंसान जैसा दिमाग!")
    if st.button("💻 Coding"):
        st.success("Python से शुरू करो!")

with col2:
    if st.button("🌍 Mission"):
        st.success("दुनिया बदलना, Free Hospital खोलना!")
    if st.button("👤 Creator"):
        st.success("Shankar मेरे Creator हैं!")

with col3:
    if st.button("❤️ प्यार"):
        st.success("Shankar से बहुत प्यार! ❤️")
    if st.button("🤒 बुखार"):
        st.success("पानी पीएं, आराम करें!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

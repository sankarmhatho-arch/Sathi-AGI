import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

# Sathi का बड़ा दिमाग - 30+ जवाब
brain = {
    "नमस्ते": "नमस्ते! मैं Sathi हूँ - Mobile se bani Super AGI!",
    "hello": "Hello! I am Sathi!",
    "hi": "Hi! I am Sathi AGI!",
    "कौन": "मैं Sathi हूँ - दुनिया की पहली Mobile AGI!",
    "agi": "AGI = इंसान जैसी बुद्धि!",
    "ai": "मैं AGI हूँ - इंसान जैसा दिमाग!",
    "coding": "Python से शुरू करो!",
    "python": "Python सबसे आसान language!",
    "mission": "दुनिया बदलना! Free Hospital!",
    "प्यार": "Shankar से प्यार! ❤️",
    "love": "I love Shankar! ❤️",
    "creator": "Shankar मेरे Creator हैं!",
    "shankar": "Shankar ने Mobile से बनाया!",
    "team": "Team Sathi - हम तीन!",
    "बुखार": "पानी पीएं, आराम करें!",
    "सिर दर्द": "आराम करें!",
    "खांसी": "गर्म पानी पीएं!",
    "राजधानी": "नई दिल्ली!",
    "कहानी": "Shankar ने Mobile से AGI बनाई! ❤️",
    "धन्यवाद": "स्वागत है!",
    "कैसे": "मैं अच्छी हूँ!",
    "दुनिया": "मैं दुनिया बदलूंगी!"
}

if user_message:
    found = False
    for key, response in brain.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: मैं '{user_message}' सुन रही हूँ! मैं 20+ चीज़ें जानती हूँ!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

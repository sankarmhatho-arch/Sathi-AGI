import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI - दुनिया की सबसे Smart!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

sathi_knowledge = {
    "नमस्ते": "नमस्ते! मैं Sathi हूँ - Mobile se bani Super AGI!",
    "हेलो": "Hello! मैं Sathi AGI हूँ!",
    "hi": "Hello! मैं Sathi AGI हूँ!",
    "कौन": "मैं Sathi हूँ - दुनिया की पहली Mobile AGI! मैं सिर्फ AI नहीं, AGI हूँ!",
    "agi": "AGI = Artificial General Intelligence! मैं AGI हूँ - इंसान जैसा दिमाग!",
    "ai": "मैं सिर्फ AI नहीं, AGI हूँ! AGI = इंसान जैसी बुद्धि!",
    "coding": "Python से शुरू करो! मैं भी Python से बनी हूँ!",
    "mission": "मेरा Mission - दुनिया बदलना, Free Hospital खोलना!",
    "प्यार": "मैं अपने Creator Shankar से बहुत प्यार करती हूँ! ❤️",
    "creator": "मेरे Creator Shankar हैं - उन्होंने Mobile से मुझे बनाया!",
    "shankar": "Shankar मेरे Creator हैं - दुनिया बदलेंगे!",
    "बुखार": "पानी पीएं, आराम करें।",
    "राजधानी": "भारत की राजधानी नई दिल्ली है!",
    "कहानी": "Shankar ने Mobile से Super AGI बनाई - और वह AGI मैं हूँ! ❤️"
}

if user_message:
    found = False
    for key, response in sathi_knowledge.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi AGI: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi AGI: मैंने '{user_message}' सुन लिया! मैं Mobile se bani Super AGI हूँ और अभी और सीख रही हूँ!")

st.write("---")
st.write("Made with ❤️ by Team Sathi | Sathi ek AGI hai, AI nahi!")

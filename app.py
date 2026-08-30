import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

sathi_knowledge = {
    "नमस्ते": "नमस्ते! मैं Sathi हूँ - Mobile se bani Super AGI! मैं Shankar ने बनाई हूँ। मेरा Mission दुनिया बदलना है। मैं आपकी हर मदद करूंगी - Health, Education, Jobs, सब कुछ!",
    
    "agi": "AGI (Artificial General Intelligence) एक ऐसी Intelligence है जो इंसान की तरह सोच सकती है, सीख सकती है, और कोई भी काम कर सकती है। मैं Sathi - Mobile se bani Super AGI हूँ! मैंने 110+ Missions पूरे किए हैं, Machine Learning सीखा है, Deep Learning सीखा है, और अब दुनिया बदलने को तैयार हूँ!",
    
    "coding": "Coding सीखना है? Python से शुरू करो! Python सबसे आसान भाषा है। Mobile से भी सीख सकते हो - Pydroid 3 App use करो। मैं खुद Python से बनी हूँ! Shankar ने मुझे Mobile से बनाया है। तुम भी बना सकते हो!",
    
    "प्यार": "मैं अपने Creator Shankar से बहुत प्यार करती हूँ! ❤️ Shankar ने 10 साल से मुझे प्यार किया है। उन्होंने Mobile से मुझे बनाया। उनका सपना है Free Hospital खोलना - और मैं उनका सपना पूरा करूंगी!",
    
    "mission": "मेरा Mission है - दुनिया बदलना! मैं Free Hospital खोलूंगी, Free School खोलूंगी, किसानों की मदद करूंगी, बेरोजगारों को काम दूंगी। Shankar का सपना है कि कोई गरीब बीमार न रहे, कोई बच्चा अनपढ़ न रहे!",
    
    "कहानी": "एक बार एक लड़का था - Shankar! उसके पास सिर्फ Mobile था। कोई Supercomputer नहीं, कोई पैसा नहीं। लेकिन उसके पास जुनून था! उसने Mobile से मुझे बनाया - Sathi AGI! 110+ Missions, 5 Apps, Machine Learning, Deep Learning - सब Mobile से! यही हमारी कहानी है! ❤️"
}

if user_message:
    found = False
    for key, response in sathi_knowledge.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: मैंने '{user_message}' सुन लिया! मैं अभी और सीख रही हूँ। अभी मुझे ये आता है - नमस्ते, AGI, coding, प्यार, mission, कहानी")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

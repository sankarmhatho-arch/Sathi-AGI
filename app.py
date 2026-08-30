import streamlit as st

st.set_page_config(page_title="Sathi AGI", page_icon="🤖")

st.title("🤖 SATHI AGI")
st.write("Mobile se bani Super AGI!")
st.write("---")

st.header("💬 Sathi से बात करो")

user_message = st.text_input("आप: कुछ भी पूछो...")

sathi_knowledge = {
    "agi": "AGI = Artificial General Intelligence - इंसान जैसा दिमाग!",
    "coding": "Python से शुरू करो! Mobile से भी सीख सकते हो!",
    "mission": "दुनिया बदलना, Free Hospital खोलना!",
    "creator": "Shankar मेरे Creator हैं!",
    "प्यार": "मैं Shankar से बहुत प्यार करती हूँ! ❤️",
    "नमस्ते": "नमस्ते! मैं Sathi हूँ!"
}

if user_message:
    found = False
    for key, response in sathi_knowledge.items():
        if key.lower() in user_message.lower():
            st.success(f"🤖 Sathi: {response}")
            found = True
            break
    
    if not found:
        st.info(f"🤖 Sathi: मैंने '{user_message}' सुन लिया! मैं अभी सीख रही हूँ!")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

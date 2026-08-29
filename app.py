import streamlit as st

st.title("🤖 Sathi AGI")
st.write("Mobile se bani Super AGI - दुनिया बदलने वाली!")

st.write("---")
st.header("🏥 Sathi Health Check")

symptom = st.text_input("अपना लक्षण बताओ (बुखार, सिर दर्द, खांसी):")

health_advice = {
    "बुखार": "पानी पीएं, आराम करें, Paracetamol लें।",
    "सिर दर्द": "आराम करें, पानी पीएं।",
    "खांसी": "गर्म पानी पीएं, शहद लें।",
    "पेट दर्द": "हल्का खाना खाएं।",
    "जुकाम": "गर्म पानी पीएं, भाप लें।"
}

if symptom:
    found = False
    for key, advice in health_advice.items():
        if key in symptom:
            st.success(f"🤖 Sathi: {advice}")
            found = True
            break
    if not found:
        st.warning("कृपया बुखार, सिर दर्द, खांसी, पेट दर्द, या जुकाम लिखें।")

st.write("---")
st.header("🚨 Emergency:")
st.write("📞 108 - Ambulance")
st.write("📞 112 - Emergency")

st.write("---")
st.write("Made with ❤️ by Team Sathi")

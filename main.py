import streamlit as st
from backend import roman_to_pashto

st.set_page_config(page_title="Roman Pashto to Proper Pashto Converter", layout="centered")

st.title("📝 Roman Pashto ➝ Proper Pashto Converter")

# User input
roman_text = st.text_area("Enter Roman Pashto text:", placeholder="Sanga yee?")

if st.button("Convert"):
    if roman_text.strip():
        with st.spinner("Converting... Please wait ⏳"):
            pashto_text = roman_to_pashto(roman_text)
        st.success("✅ Converted Text:")
        st.write(pashto_text)
    else:
        st.warning("⚠️ Please enter some text to convert.")

st.markdown("Built with **Langchain + Groq API + Streamlit**")

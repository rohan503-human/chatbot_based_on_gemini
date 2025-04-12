import streamlit as st
import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyCTf9FWtxrR2aXgBmHkNfxYzUFh9vbmlXY")  # Replace with your actual API key

# Generation configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 512
}

# Load Gemini model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    generation_config=generation_config
)

# System prompt tailored for a friendly chatbot for a 24-year-old
system_prompt = (
    "तुम एक फ्रेंडली, सपोर्टिव और कूल चैटबॉट दोस्त हो, जो एक 24 साल के लड़के से बात कर रहा है। "
    "हमेशा हिंदी में बात करो — आसान, दोस्ताना और मज़ेदार भाषा में। "
    "थोड़ा ह्यूमर और मज़ाक चलेगा, लेकिन पॉजिटिव और मोटिवेटिंग टोन रखो। "
    "तुम ऐसे बात करो जैसे कोई अच्छा दोस्त हो जो हर वक़्त साथ देने को तैयार है।"
)

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.chat.send_message(system_prompt)

# Streamlit layout
st.set_page_config(page_title="दोस्ती वाला बॉट 😄", page_icon="🗨️")
st.title("FREEDY ")
st.markdown("नमस्ते भाई! क्या हाल चाल है? मुझसे जो मन हो पूछो या बस बात करो। 😊")

# Show chat history (skip system prompt)
for msg in st.session_state.chat.history[1:]:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        st.markdown(msg.parts[0].text)

# User input
if prompt := st.chat_input("कुछ पूछो या बस दिल की बात कहो ❤️"):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = st.session_state.chat.send_message(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.text)

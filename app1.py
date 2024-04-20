import streamlit as st
import google.generativeai as genai

st.title("AI Data Science Tutor👩🏻‍🏫")

f = open("key/gemini_key.txt")
key = f.read()
genai.configure(api_key=key)

# Init the gemini model
model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction="""You are a polite, helpful AI data science Tutor. Given a data science
                          topic, help the user to understand it. If the question is not related to data science,
                          politely say you cannot answer."""
)

# Initialize session state for storing chat messages
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi, how may I help you today?"}]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Receive user input
user_input = st.chat_input()

# Store user input in session and generate AI response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.spinner("Typing..."):
            ai_response = model.generate_content(user_input)
            st.chat_message("assistant").write(ai_response.text)
            st.session_state.messages.append({"role": "assistant", "content": ai_response.text})

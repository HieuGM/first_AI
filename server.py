import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["Key"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Chat with GM-AI")

# session_state để lưu hội thoại
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# hiển thị chat cũ
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

user_input = st.chat_input("Type something...")
if user_input:
    # hiển thị tin nhắn người dùng
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    response = model.generate_content(user_input)
    reply = response.text

    st.chat_message("bot").markdown(reply)
    st.session_state["messages"].append({"role": "bot", "content": reply})

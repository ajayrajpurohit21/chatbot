import os
import streamlit as st
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.set_page_config(page_title="Gemini AI Chat", layout="centered")
st.title("🤖 Gemini AI Chatbot")
st.markdown("Ask something and Gemini will reply...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your question here...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            ),
        )
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    st.session_state.chat_history.append(("Gemini", bot_reply))

st.divider()
st.subheader("🧵 Chat History")

for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Gemini:** {msg}")

import streamlit as st
from main import run_agent
import time

# page configuration 

# 🔹 Page setup
st.set_page_config(page_title="Travel Agent", page_icon="✈️")

st.title("✈️ Travel Agent")

# 🔹 Initialize chat history (memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🔹 Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# user input

user_input = st.chat_input("Ask me anything You want to know about Travelling...")



if user_input:
    if "last_input" not in st.session_state or st.session_state.last_input != user_input:
        st.session_state.last_input = user_input

        # store user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = run_agent(user_input)
        except Exception:
            response = "⚠️ Server busy. Try again in a few seconds."

        # store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()
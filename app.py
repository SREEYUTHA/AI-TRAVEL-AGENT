import streamlit as st
from main import run_agent
import time
import traceback
import base64

# page configuration 

# 🔹 Page setup
st.set_page_config(page_title="Travel Agent", page_icon="✈️")

# 🔹 Background image
with open("assets/train2.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .travel-title {{
        text-align: center;
        font-size: 70px;
        font-weight: 900;
        font-family: Gerogia, serif;
        font-style: italic;
        color: white;
        margin-top: 150px;
        margin-bottom: 100px;
        text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.7);
    }}

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="travel-title">
        ✈️ Travel Agent
    </div>
    """,
    unsafe_allow_html=True
)
# st.title("✈️ Travel Agent")

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
        except Exception as e:
            # response = "⚠️ Server busy. Try again in a few seconds."
            response = f"⚠️ Error: {e}"


        # store assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()
# app.py
import os

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["AI_GATEWAY_API_KEY"],
    base_url="https://ai-gateway.vercel.sh/v1",
)
MODEL = "google/gemma-4-26b-a4b-it"

st.title("Mini chatbot con AI Gateway")

# Streamlit rilegge tutto lo script a ogni interazione: la cronologia va in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ridisegna i messaggi già scambiati
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# casella di input in fondo alla pagina
if domanda := st.chat_input("Scrivi un messaggio"):
    st.session_state.messages.append({"role": "user", "content": domanda})
    with st.chat_message("user"):
        st.write(domanda)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Sei un assistente simpatico. Rispondi in italiano, in modo breve.",
            },
            *st.session_state.messages,
        ],
    )
    risposta = response.choices[0].message.content or ""

    st.session_state.messages.append({"role": "assistant", "content": risposta})
    with st.chat_message("assistant"):
        st.write(risposta)

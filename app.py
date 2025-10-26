import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("💬 CodingTrix GPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.markdown(prompt)
    reply = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":m["role"],"content":m["content"]} for m in st.session_state.messages]
    )
    answer = reply.choices[0].message.content
    st.session_state.messages.append({"role":"assistant","content":answer})
    with st.chat_message("assistant"): st.markdown(answer)

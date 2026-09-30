import ollama
import streamlit as st
st.title("My to my ChatBot App!!!")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
        {"role": "user",
         "content": question}
        
    )
    
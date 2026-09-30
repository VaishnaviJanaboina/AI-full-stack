import ollama
import streamlit as st
st.title(":green[WELCOME TO MY CHATBOT!!!🙏]")
st.write("Hi, *Guys!* :sunglasses:")

with st.sidebar:
        st.header(":blue[Chat Settings ⚙️]")
        if st.button("Del Chat 🧺"):
                    st.session_state.messages = []
                    st.success("Chat del ✅")
        uploaded_file = st.file_uploader("upload a text file..")
        personalities = {
              "Kid 👧" : "Answer the questions like you are explaining to a 5 year old kid in 2 lines only",
              "Friend 🧑🏻‍🤝‍🧑🏻" : "Answer the questions in friendly and casual manner. give in 5 lines",
              "Teacher 👨‍🏫" : "Answer the questions in heigh level and in 10 lines"
        }
        personality = st.selectbox("select a personality", personalities.keys())
        uploaded_file = st.file_uploader("upload a text file...")
        try:
              if uploaded_file:
                    content = uploaded_file.read().decode("utf-8")
                    st.success("file uploaded successfully..")
                    if st.button("Display"):
                        st.text(content)
        except:
              st.error("It is not text file")

        
        if uploaded_file:
                st.write("file uploaded successfully!!")
                if st.button("Display"):
                    context = uploaded_file.read().decode("utf-8")
                    st.text(context)
        st.write("Hi, *Guys!* :sunglasses:")
        st.header("Chat Settings")
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
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        response =ollama.chat(
            model= "llama3.2:3b",
                messages = [
                    {"role": "system","content": personalities[personality]}]
                    +st.session_state.messages)
        
    st.session_state.messages.append(
            {"role":"assistant",
            "content":response["message"]["content"]
            }
        )
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])
        

    
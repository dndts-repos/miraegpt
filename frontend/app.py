import streamlit as st
import requests

LLM_URL = "http://localhost:8000/gpt/invoke"

def generate_response(initial_message: str):
    request_body = {"input" : {"initial_message": initial_message}}
    response = requests.post(LLM_URL, json=request_body)
    if response.status_code == 200:
        response_body = response.json()
        try:
            output = response_body['output']
            answer = output['response']
            return answer        
        except:
            return "I'm sorry, I am unable to answer your question. Try again!"
    else:
        return response.text

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write(generate_response(prompt))

    st.session_state.messages.append({"role": "assistant", "content": response})

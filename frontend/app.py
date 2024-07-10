from typing import List
from groq import BaseModel
import streamlit as st
import requests
from langchain_core.documents import Document

LLM_URL = "http://localhost:8000/gpt/invoke"

class Output(BaseModel):
    current_message: str =''
    issue_type: str = ''
    chat_histories: List[tuple[str, str]] = []
    summary: str = ''
    reply: str = ''
    chunks: List[Document] = []

def generate_response(current_message: str, graph_state):
    request_body = {"input" : {
        "current_message": current_message,
        "issue_type": graph_state['issue_type'],
        "chat_histories": graph_state['chat_histories'],
        "summary": graph_state['summary'],
        "reply": graph_state['reply'],
        "chunks": graph_state['chunks']
    }}
    response = requests.post(LLM_URL, json=request_body)
    if response.status_code == 200:
        response_body = response.json()
        try:
            output = response_body['output']
            return output
        except:
            return "I'm sorry, I am unable to answer your question. Try again!"
    else:
        return Output(reply=response.text)


def get_sources(chunks):
    sources = set()
    for chunk in chunks:
        source = chunk['metadata']['source']
        sources.add(source.split('/')[-1].split(' ')[0])
    return sources

if "messages" not in st.session_state:
    st.session_state.messages = []

if "graph_state" not in st.session_state:
    st.session_state.graph_state = {
        'current_message': '',
        'issue_type': '',
        'chat_histories': [],
        'summary': '',
        'reply': '',
        'chunks': []
    }

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        new_graph_state = generate_response(prompt, st.session_state.graph_state)
        st.session_state.graph_state = new_graph_state
        response = new_graph_state['reply']
        sources = get_sources(new_graph_state['chunks'])
        response = response + '\n\n' + "Reference sources: " + ', '.join(sources)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
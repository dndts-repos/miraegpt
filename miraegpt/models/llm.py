from dotenv import load_dotenv
import os
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

MAX_LLM_RETRIES = 3

LLAMA = 'llama3'
LLAMA_INSTRUCT = 'llama3:8b-instruct-q8_0'
GROQ_LLAMA = 'llama3-70b-8192'
EMBEDDER = 'mxbai-embed-large'

LLAMA_LLM = Ollama(model=LLAMA)
EMBEDDER_LLM = OllamaEmbeddings(model=EMBEDDER)
TOOL_LLAMA_LLM = OllamaFunctions(model=LLAMA_INSTRUCT)
GROQ_LLM = ChatGroq(model=GROQ_LLAMA, api_key=GROQ_API_KEY)
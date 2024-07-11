from dotenv import load_dotenv
import os
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')

MAX_LLM_RETRIES = 3

LLAMA = 'llama3'
LLAMA_INSTRUCT = 'llama3:8b-instruct-q8_0'
GROQ_LLAMA = 'llama3-70b-8192'
GROQ_SMALL_LLAMA = 'llama3-8b-8192'
EMBEDDER = 'mxbai-embed-large'

# LLAMA_LLM = Ollama(model=GROQ_SMALL_LLAMA)
LLAMA_LLM = ChatGroq(model=GROQ_SMALL_LLAMA, api_key=GROQ_API_KEY)
EMBEDDER_LLM = OllamaEmbeddings(model=EMBEDDER, base_url=OLLAMA_URL)
# TOOL_LLAMA_LLM = OllamaFunctions(model=GROQ_SMALL_LLAMA)
TOOL_LLAMA_LLM = ChatGroq(model=GROQ_LLAMA, api_key=GROQ_API_KEY)
GROQ_LLM = ChatGroq(model=GROQ_LLAMA, api_key=GROQ_API_KEY)
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings

LLAMA = "llama3:8b-instruct-q8_0"
EMBEDDER = 'mxbai-embed-large'

LLAMA_LLM = Ollama(model=LLAMA)

EMBEDDER_LLM = OllamaEmbeddings(model=EMBEDDER)

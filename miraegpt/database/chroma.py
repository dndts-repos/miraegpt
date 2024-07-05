import os
from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

from miraegpt.models.llm import EMBEDDER_LLM

CHROMA_PATH = os.path.join("data", "chroma")
CHROMA_READ_FILE = "summary"
CHROMA_PERSIST_FILE = "summary_v0.2"

persist_dir = os.path.join(CHROMA_PATH, CHROMA_PERSIST_FILE)

vectorstore = Chroma(persist_directory=persist_dir, embedding_function=EMBEDDER_LLM)

retriever: VectorStoreRetriever = vectorstore.as_retriever(search_kwargs={"k": 3})
import os
import chromadb
from chromadb.config import Settings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from miraegpt.chains.category_judge import recursive_judge_invoke
from miraegpt.chains.message_categorizer import recursive_generator_invoke
from miraegpt.models.llm import EMBEDDER_LLM
from miraegpt.database.chroma import (
    CHROMA_PATH,
    CHROMA_PERSIST_FILE as CHROMA_WRITE_FILE,
    CHROMA_READ_FILE
)

read_client = chromadb.Client(
    Settings(
        is_persistent=True, 
        persist_directory=os.path.join(CHROMA_PATH, CHROMA_READ_FILE)
    )
)

db = Chroma(
    persist_directory=os.path.join(CHROMA_PATH, CHROMA_WRITE_FILE), 
    embedding_function=EMBEDDER_LLM
)

if __name__ == '__main__':
    collection = read_client.get_collection('langchain')
    data = collection.get()
    documents = data["documents"]
    metadatas = data["metadatas"]
    new_documents = []
    for i, doc in enumerate(documents):
        clean_doc = doc.split(':')[-1].strip()
        categories = recursive_generator_invoke(clean_doc)
        if len(categories) > 1:
            category = recursive_judge_invoke(clean_doc, categories)
        else:
            category = categories[0]
        metadatas[i]['category'] = category
        new_documents.append(Document(page_content=clean_doc, metadata=metadatas[i]))
        print(clean_doc)
        print(f"Generated: {categories}")
        print(f"Judge: {category}")
        print('-'*100)

    db.add_documents(new_documents)

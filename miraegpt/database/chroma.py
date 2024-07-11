import os
from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

from miraegpt.models.llm import EMBEDDER_LLM

TEMPLATES_COLLECTION_NAME = 'templates'
CATEGORIES = ('technical', 'delivery', 'accessories')
CHROMA_TEMPLATES_PATH = os.path.join('miraegpt', 'data', 'chroma', TEMPLATES_COLLECTION_NAME)

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 512

def load_word_documents(path_to_word_documents: str) -> list[Document]:
    documents: list[Document] = []
    word_documents = os.listdir(path_to_word_documents)
    for filename in word_documents:
        word_document_path = os.path.join(path_to_word_documents, filename)
        result = UnstructuredWordDocumentLoader(word_document_path).load()
        for document in result:
            source: str = document.metadata['source']
            issue = source.split(' ')[-1].split('.')[0]
            document.metadata['issue_type'] = issue
            documents.append(document)
    return documents

def chunk_documents(documents: list[Document], chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)

    prev_chunk = Document(page_content="", metadata={'source':''})
    chunks_ids: list[str] = []
    for chunk in chunks:
        source = chunk.metadata['source']
        prev_source = prev_chunk.metadata['source']
        if source != prev_source:
            part = 1
        else:
            part = prev_chunk.metadata['part'] + 1

        id = f'{part}-{source}'
        chunk.metadata['part'] = part
        chunk.metadata['id'] = id
        chunks_ids.append(id)
        prev_chunk = chunk
    return chunks, chunks_ids


def write_to_vectorstore(
    persist_dir: str, 
    chunks: list[Document], 
    chunks_ids: list[str], 
    collection_name: str,
    embedding = EMBEDDER_LLM
) -> Chroma:
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        collection_name=collection_name,
        ids=chunks_ids,
        persist_directory=persist_dir
    )

def connect_to_vectorstore(
    collection_name: str,
    persist_dir: str,
    embedding = EMBEDDER_LLM
):
    return Chroma(
        collection_name=collection_name, 
        embedding_function=embedding, 
        persist_directory=persist_dir
    )


if __name__ == '__main__':
    for category in CATEGORIES:
        path_to_word_documents = os.path.join('miraegpt', 'data', 'templates', category)
        documents = load_word_documents(path_to_word_documents)
        chunks, chunks_ids = chunk_documents(documents)
        write_to_vectorstore(
            persist_dir=CHROMA_TEMPLATES_PATH, 
            chunks=chunks, 
            chunks_ids=chunks_ids,
            collection_name=TEMPLATES_COLLECTION_NAME
        )
        db = connect_to_vectorstore(
            collection_name=TEMPLATES_COLLECTION_NAME,
            persist_dir=CHROMA_TEMPLATES_PATH
        )
    print(len(db))
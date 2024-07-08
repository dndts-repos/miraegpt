
from miraegpt.database.chroma import CHROMA_TEMPLATES_PATH, TEMPLATES_COLLECTION_NAME, connect_to_vectorstore
from miraegpt.langgraph.state import GraphState


NAME = "Retriever"

def retrieve(state: GraphState):
    issue = state["issue_type"]
    message = state["current_message"]
    db = connect_to_vectorstore(
        collection_name=TEMPLATES_COLLECTION_NAME,
        persist_dir=CHROMA_TEMPLATES_PATH
    )
    documents = db.similarity_search(message, k=1, filter={'issue_type': issue})
    return {'chunks': documents}


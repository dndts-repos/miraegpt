
from miraegpt.database.chroma import CHROMA_TEMPLATES_PATH, TEMPLATES_COLLECTION_NAME, connect_to_vectorstore
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


NAME = "Retriever"

def retrieve(state: GraphState):
    issue = state["issue_type"]
    message = state["current_message"]
    db = connect_to_vectorstore(
        collection_name=TEMPLATES_COLLECTION_NAME,
        persist_dir=CHROMA_TEMPLATES_PATH
    )
    documents = db.similarity_search(message, k=2, filter={'issue_type': issue})
    write_markdown_file(f'Documents: {documents}', "retriever")
    return {'chunks': documents}


if __name__ == '__main__':
    question = 'My phone is locked. I do not have the password'
    state: GraphState = GraphState(current_message=question, issue_type='Pin')
    response = retrieve(state)
    chunks = response['chunks']
    for chunk in chunks:
        print(chunk.page_content)
        print(f'metadata: {chunk.metadata}')
        print('-'*100)
from typing_extensions import TypedDict
from typing import List, Literal
from langchain_core.documents import Document

class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """
    current_message: str
    issue_type: str
    chat_histories: List[tuple[str, str]] 
    summary: str
    reply: str
    chunks: List[Document]
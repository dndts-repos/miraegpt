from typing_extensions import TypedDict
from typing import List, Literal
from langchain_core.documents import Document

class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """
    current_message: str
    reply_type: Literal['Information', 'Email']
    issue_type: str
    chat_histories: list[str]
    summary: str = ''
    reply: str
    chunks: List[Document]
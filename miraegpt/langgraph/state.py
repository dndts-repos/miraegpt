from typing_extensions import TypedDict
from typing import List
from langchain_core.documents import Document

class GraphState(TypedDict):
     """
    Represents the state of our graph.

    Attributes:
        initial_message: message
        category: issue category
        response: LLM generation
        context: list of documents
        num_steps: number of steps
    """
     initial_message: str
     category: str
     response: str
     chat_histories: list[list[Document]]
     most_relevent_chat_history: list[Document]
     context: List[str]
     num_steps: int
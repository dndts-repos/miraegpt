
from typing import List
from fastapi import FastAPI
from langchain.pydantic_v1 import BaseModel
from langserve import add_routes
from miraegpt.langgraph.build import miraegpt
from langchain_core.documents import Document

class Input(BaseModel):
    current_message: str =''
    issue_type: str = ''
    chat_histories: List[tuple[str, str]] = []
    summary: str = ''
    reply: str = ''
    chunks: List[Document] = []

class Output(BaseModel):
    current_message: str =''
    issue_type: str = ''
    chat_histories: List[tuple[str, str]] 
    summary: str = ''
    reply: str = ''
    chunks: List[Document] = []

app = FastAPI(
    title="miraeGPT Server",
    version="1.0",
    description="API server using miraeGPT"
)

add_routes(
    app,
    miraegpt,
    path='/gpt',
    input_type=Input,
    output_type=Output
)
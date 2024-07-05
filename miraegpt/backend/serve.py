
from fastapi import FastAPI
from langchain.pydantic_v1 import BaseModel
from langserve import add_routes
from miraegpt.langgraph.build import miraegpt

class Input(BaseModel):
    initial_message: str
    num_steps: int = 0

class Output(BaseModel):
    response: str

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
from typing import Literal
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables.utils import Input
from langchain_core.exceptions import OutputParserException
from langchain_core.runnables import RunnableLambda

from miraegpt.models.llm import MAX_LLM_RETRIES, TOOL_LLAMA_LLM

USER_INPUT_KEY = 'question'

class ReponseType(BaseModel):
    value: Literal['Information', 'Email'] = Field(
        ...,
        description="Given a user input, determine if user wants reply as Email or just a General Answer."
    )

prompt = PromptTemplate(
    template="""
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are part of a large language model pipeline that would response to a user input with either pure information or an email.
    You are specialised in understanding text input provided by a user and determine what finally outcome the user desires.
    You should reply either
        Email - if user want the pipeline to craft an email 
        or 
        Information - if user do not want an email crafted and just want the pipeline to give a general information.<|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    User Input: {question}<|eot_id|>

    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[USER_INPUT_KEY]
)

'''
In the event where the LLM is unable to provide a response,
which maybe due to some OutputParserException or ValueError,
the Response Type would be defaulted to 'Information'.
'''
def response_type_fallback(inputs: Input):
    print('----- Response Type Chain: Invoking Fallback -----')
    return ReponseType(value='Information')

RESPONSE_TYPE_LLM = TOOL_LLAMA_LLM\
    .with_structured_output(ReponseType)\
    .with_retry(retry_if_exception_type=(OutputParserException, ValueError), stop_after_attempt=MAX_LLM_RETRIES)\
    .with_fallbacks([RunnableLambda(response_type_fallback)])

RESPONSE_TYPE_CHAIN = prompt | RESPONSE_TYPE_LLM
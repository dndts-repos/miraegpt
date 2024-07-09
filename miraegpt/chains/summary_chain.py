from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from miraegpt.models.llm import LLAMA_LLM

CHAT_HISTORY_KEY = 'history'
SUMMARY_KEY = 'summary'

prompt = PromptTemplate(
    template="""
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are part of a large language model pipeline that would response to a user input with answers.
    You are assisting a company's customer service personel with their daily task. 
    The company is a second hand phone retailer that ships and sells phones in Europe. When the customer received their phones, they may face some difficulties or issues with their phones. 
    The customer service personel's job is to assist the customer in solving their problem with the lowest cost possible.
    
    You will be given 
        1. Chat History - The exact conversation between you and the customer service personel, at most 3 question-and-answer between you and the customer service personel.
        2. Summary - The summarized chat history between you and the customer service personel right from the beginning.
    Your role is to understand the context of the your conversation with the customer service personel with the chat history and summary provided, 
    and summarise the latest conversations from the chat history together with the summary. 
    <|start_header_id|>user<|end_header_id|>
    Chat History: 
    {history}
    Summary: {summary}<|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[CHAT_HISTORY_KEY, SUMMARY_KEY]
)

SUMMARY_CHAIN = prompt | LLAMA_LLM | StrOutputParser()
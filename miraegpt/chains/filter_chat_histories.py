from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

from miraegpt.models.llm import LLAMA_LLM

MESSAGE_KEY = 'initial_message'
CHAT_1 = 'chat_history_1'
CHAT_2 = 'chat_history_2'

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a master at understanding message and matching it to the most relevent chat history.
    You will be given an initial message and 2 chat histories. Your job is to choose the chat history that most resembles the initial message.

    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Conduct a comprehensive analysis of the initial message and 2 chat histories provided, 
    Return either 1 or 2 depending on which chat history you chose,
    example if the first chat is more relevant:
        1
    
    DO NOT add any premable or explanation
        
    Initial Message:\n\n{initial_message}\n\n
    Chat History 1: \n\n{chat_history_1}\n\n
    Chat History 2: \n\n{chat_history_2}\n\n
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[MESSAGE_KEY, CHAT_1, CHAT_2],
)

filter_chat_history_generator = prompt | LLAMA_LLM | StrOutputParser()

def recursive_filter_invoke(initial_message: str, chat_history_1: str, chat_history_2: str):
    try:
        chat_number = int(filter_chat_history_generator.invoke({
            MESSAGE_KEY: initial_message,
            CHAT_1: chat_history_1,
            CHAT_2: chat_history_2
        }))
        return chat_number
    except:
        print('Filter Output Invalid!\nretrying...')
        return recursive_filter_invoke(initial_message, chat_history_1, chat_history_2)
    
def filter_chat_histories(chat_histories: list[list[Document]], initial_message: str) -> list[Document]:
    first_chat = chat_histories[0]
    for i in range(1, len(chat_histories)):
        second_chat = chat_histories[i]
        winner: int = recursive_filter_invoke(initial_message, first_chat, second_chat)
        if winner == 2:
            first_chat = second_chat
    return first_chat

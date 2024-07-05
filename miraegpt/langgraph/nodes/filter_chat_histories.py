from langchain_core.documents import Document

from miraegpt.chains.filter_chat_histories import filter_chat_histories
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


def get_most_relevent_chat_history(state: GraphState):
    print("---Retrieving Most Relevent Chat History---")
    initial_message = state['initial_message']
    chat_histories = state['chat_histories']
    num_steps = int(state['num_steps'])
    num_steps += 1

    chat_history = filter_chat_histories(chat_histories, initial_message)
    write_markdown_file(style(chat_history), "category")

    return {"most_relevent_chat_history": chat_history, "num_steps" : num_steps}

def style(chat_history: list[Document]):
    result = ''
    for chat in chat_history:
        sender = chat.metadata['sender']
        content = chat.page_content
        result += f'{sender}:\n{content}\n\n'
    return result
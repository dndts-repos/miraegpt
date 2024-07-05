from miraegpt.chains.unrelated_chain import (
    SUMMARY_KEY,
    UNRELATED_CHAIN,
    USER_INPUT_KEY
)
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import manage_chat_histories, write_markdown_file

HANDLER_NAME = "Unrelated Handler"

def handle(state: GraphState):
    """Reply any unrelated questions pertaining to Ecomms"""
    print(f'----- {HANDLER_NAME}: GENERATING REPLY -----')
    
    user_input = state["current_message"]
    summary = state['summary']
    response = UNRELATED_CHAIN.invoke({USER_INPUT_KEY: user_input, SUMMARY_KEY: summary})
    print(f'----- {HANDLER_NAME}: REPLY GENERATED -----')
    write_markdown_file(response, "unrelated_handler")

    chat_history = manage_chat_histories(state['chat_histories'], user_input, response)

    return {'reply': response, 'chat_histories': chat_history}
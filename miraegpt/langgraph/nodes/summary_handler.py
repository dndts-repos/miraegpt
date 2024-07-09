from miraegpt.chains.summary_chain import (
    CHAT_HISTORY_KEY,
    SUMMARY_CHAIN,
    SUMMARY_KEY
)
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file

HANDLER_NAME = "Summary Handler"

def handle(state: GraphState):
    """Summarised the chat history between LLM and Ecomms"""
    print(f'----- {HANDLER_NAME}: SUMMARISING CHAT HISTORIES -----')

    chat_histories = state['chat_histories']
    summary = state['summary']
    response = SUMMARY_CHAIN.invoke({CHAT_HISTORY_KEY: chat_histories, SUMMARY_KEY: summary})
    print(f'----- {HANDLER_NAME}: CHAT HISTORIES SUMMARISED -----')
    write_markdown_file(response, "summary_handler")

    return {'summary': response}
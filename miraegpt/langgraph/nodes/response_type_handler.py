from miraegpt.chains.response_type_chain import (
    RESPONSE_TYPE_CHAIN,
    USER_INPUT_KEY,
    ReponseType
)
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file

HANDLER_NAME = "Response Type Handler"

def handle(state: GraphState):
    """Decides whether the reply is going to be a Email or get a general answer"""
    print(f'----- {HANDLER_NAME}: DECIDING TO REPLY IN EMAIL OR NOT -----')
    user_input = state['current_message']

    response: ReponseType = RESPONSE_TYPE_CHAIN.invoke({USER_INPUT_KEY: user_input})
    response_type = response.value
    write_markdown_file(f'Response Type: {response_type}', "response_type_handler")
    print(f'----- {HANDLER_NAME}: DECIDED TO REPLY AS [{response_type}] -----')

    return {'reply_type': response_type}
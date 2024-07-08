from miraegpt.chains.email_chain import DOCUMENTS_KEY, EMAIL_CHAIN, QUESTION_KEY
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


HANDLER_NAME = "Information Handler"

def handle(state: GraphState):
    """Help to write a step-by-step guide for customer service personel given the user input/question"""
    print(f'----- {HANDLER_NAME}: SUMMARISING DOCUMENTS -----')
    question = state['current_message']
    chunks = state['chunks']
    documents = ''
    for chunk in chunks:
        documents += chunk.page_content + '\n\n'
    response = EMAIL_CHAIN.invoke({QUESTION_KEY: question, DOCUMENTS_KEY: documents})
    write_markdown_file(f'Reply: {response}', "information_handler")
    print(f'----- {HANDLER_NAME}: DOCUMENTS SUMMARISED AND STEPS LISTED -----')

    return {'reply': response}

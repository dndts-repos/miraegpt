from miraegpt.chains.email_chain import DOCUMENTS_KEY, EMAIL_CHAIN, QUESTION_KEY
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


HANDLER_NAME = "Email Handler"

def handle(state: GraphState):
    """Help to write an email-like reply given the user input/question"""
    print(f'----- {HANDLER_NAME}: WRITING EMAIL -----')
    question = state['current_message']
    chunks = state['chunks']
    documents = ''
    for chunk in chunks:
        documents += chunk.page_content + '\n\n'
    response = EMAIL_CHAIN.invoke({QUESTION_KEY: question, DOCUMENTS_KEY: documents})
    write_markdown_file(f'Reply: {response}', "email_handler")
    print(f'----- {HANDLER_NAME}: EMAIL WRITTEN -----')

    return {'reply': response}

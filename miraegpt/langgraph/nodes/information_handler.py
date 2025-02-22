from miraegpt.chains.information_chain import INFORMATION_CHAIN, DOCUMENTS_KEY, QUESTION_KEY, SUMMARY_KEY
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import manage_chat_histories, write_markdown_file


HANDLER_NAME = "Information Handler"

def handle(state: GraphState):
    """Help to write a step-by-step guide for customer service personel given the user input/question"""
    print(f'----- {HANDLER_NAME}: SUMMARISING DOCUMENTS -----')
    question = state['current_message']
    chunks = state['chunks']
    summary = state['summary']
    chat_histories = state['chat_histories']
    documents = ''
    for chunk in chunks:
        documents += chunk.page_content + '\n\n'
    response = INFORMATION_CHAIN.invoke({
        QUESTION_KEY: question, 
        DOCUMENTS_KEY: documents, 
        SUMMARY_KEY: summary,
    })
    write_markdown_file(f'Reply: {response}', "information_handler")
    print(f'----- {HANDLER_NAME}: DOCUMENTS SUMMARISED AND STEPS LISTED -----')

    chat_histories = state['chat_histories']

    chat_history = manage_chat_histories(chat_histories, question, response)

    return {'reply': response, 'chat_histories': chat_history}

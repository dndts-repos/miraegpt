from miraegpt.chains.query_rewrite_chain import QUERY_REWRITE_CHAIN, QUESTION_KEY, SUMMARY_KEY
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


HANDLER_NAME = "Query Rewrite Handler"

def handle(state: GraphState):
    """Help to rewrite user input/question"""
    print(f'----- {HANDLER_NAME}: REWRITING USER INPUT -----')
    question = state['current_message']
    summary = state['summary']
    response = QUERY_REWRITE_CHAIN.invoke({
        QUESTION_KEY: question, 
        SUMMARY_KEY: summary,
    })
    write_markdown_file(f'Rewritten Message: {response}', "query_rewrite")
    print(f'----- {HANDLER_NAME}: REWRITTEN USER INPUT -----')

    return {'current_message': response}
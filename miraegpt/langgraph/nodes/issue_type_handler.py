from miraegpt.chains.issues_type_chain import ISSUE_TYPE_CHAIN, QUESTION_KEY, IssueType
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file

HANDLER_NAME = "Issue Type Handler"

def handle(state: GraphState):
    """Determines the issue type based on the user's questions"""
    print(f'----- {HANDLER_NAME}: DETERMINING THE ISSUE TYPE -----')
    
    issue_type = state["issue_type"]
    if issue_type:
        return {'issue_type': issue_type}
    question = state["current_message"]
    response: IssueType = ISSUE_TYPE_CHAIN.invoke({QUESTION_KEY: question})
    issue_type = response.value
    write_markdown_file(f'Issue Type: {issue_type}', "issue_type_handler")
    print(f'----- {HANDLER_NAME}: DETERMINED ISSUE TYPE AS [{issue_type}] -----')

    return {'issue_type': issue_type}
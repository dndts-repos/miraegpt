from langgraph.graph import END, StateGraph
from miraegpt.langgraph.state import GraphState
import miraegpt.langgraph.nodes.response_type_handler as response_type_handler
import miraegpt.langgraph.nodes.issue_type_handler as issue_type_handler
import miraegpt.langgraph.nodes.information_handler as information_handler
import miraegpt.langgraph.nodes.email_handler as email_handler
import miraegpt.langgraph.nodes.unrelated_handler as unrelated_handler
import miraegpt.langgraph.nodes.summary_handler as summary_handler
from miraegpt.langgraph.nodes.retriever import retrieve
from miraegpt.langgraph.nodes.printer import state_printer

workflow = StateGraph(GraphState)

GENERAL_CLASSIFIER = 'general classifier'
ISSUES_CLASSIFIER = 'issue classifier'
INFORMATION_HANDLER = 'information handler'
EMAIL_HANDLER = 'email handler'
UNRELATED_HANDLER = 'unrelated handler'
SUMMARY_HANDLER = 'summary handler'
RETRIEVER = 'retriever'

def unrelated_check(state: GraphState):
    issue = state['issue_type']
    if issue == 'Unrelated':
        return UNRELATED_HANDLER
    return RETRIEVER

def email_check(state: GraphState):
    reply_type = state['reply_type']
    if reply_type == 'Email':
        return EMAIL_HANDLER
    return INFORMATION_HANDLER

# Add Nodes
workflow.add_node(GENERAL_CLASSIFIER, response_type_handler.handle)
workflow.add_node(ISSUES_CLASSIFIER, issue_type_handler.handle)
workflow.add_node(INFORMATION_HANDLER, information_handler.handle)
workflow.add_node(EMAIL_HANDLER, email_handler.handle)
workflow.add_node(UNRELATED_HANDLER, unrelated_handler.handle)
workflow.add_node(SUMMARY_HANDLER, summary_handler.handle)
workflow.add_node(RETRIEVER, retrieve)

# Create Edges
workflow.set_entry_point(GENERAL_CLASSIFIER)
workflow.add_edge(GENERAL_CLASSIFIER, ISSUES_CLASSIFIER)
workflow.add_conditional_edges(ISSUES_CLASSIFIER, unrelated_check)
workflow.add_conditional_edges(RETRIEVER, email_check)
workflow.add_edge(UNRELATED_HANDLER, SUMMARY_HANDLER)
workflow.add_edge(INFORMATION_HANDLER, SUMMARY_HANDLER)
workflow.add_edge(EMAIL_HANDLER, SUMMARY_HANDLER)
workflow.add_edge(SUMMARY_HANDLER, END)

miraegpt = workflow.compile()

if __name__ == "__main__":
    question = 'I need your help to craft an email. The customer said that the battery health is terrible. They want to replace the phone.'
    print(miraegpt.invoke({'current_message': question}))

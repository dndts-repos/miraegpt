from langgraph.graph import END, StateGraph
from miraegpt.langgraph.nodes.filter_chat_histories import get_most_relevent_chat_history
from miraegpt.langgraph.nodes.retrieval import retrieve_documents
from miraegpt.langgraph.nodes.writer import reply
from miraegpt.langgraph.nodes.categorizer import categorize_message
from miraegpt.langgraph.nodes.printer import state_printer
from miraegpt.langgraph.state import GraphState

workflow = StateGraph(GraphState)

CATEGORIZER = "categorize_message"
RETRIEVAL = "retrieval"
FILTER_CHAT_HISTORY = "filter_chat_history"
WRITER = "writer"
PRINTER = "state_printer"

# Add Nodes
workflow.add_node(CATEGORIZER, categorize_message)
workflow.add_node(RETRIEVAL, retrieve_documents)
workflow.add_node(FILTER_CHAT_HISTORY, get_most_relevent_chat_history)
workflow.add_node(WRITER, reply)
workflow.add_node(PRINTER, state_printer)

# Create Edges
workflow.set_entry_point(CATEGORIZER)
workflow.add_edge(CATEGORIZER, RETRIEVAL)
workflow.add_edge(RETRIEVAL, FILTER_CHAT_HISTORY)
workflow.add_edge(FILTER_CHAT_HISTORY, WRITER)
workflow.add_edge(WRITER, PRINTER)
workflow.add_edge(PRINTER, END)

miraegpt = workflow.compile()

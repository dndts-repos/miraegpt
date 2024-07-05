from miraegpt.libs.utils import write_markdown_file
from miraegpt.chains.message_categorizer import recursive_generator_invoke
from miraegpt.chains.category_judge import recursive_judge_invoke
from miraegpt.langgraph.state import GraphState

def categorize_message(state: GraphState):
    """take initial message and categorize it"""
    print("---CATEGORIZING INITIAL MESSAGE---")
    initial_message = state['initial_message']
    num_steps = int(state['num_steps'])
    num_steps += 1

    categories = recursive_generator_invoke(initial_message)
    top_category = recursive_judge_invoke(initial_message, categories)
    write_markdown_file(style(categories, top_category), "category")

    return {"category": top_category, "num_steps" : num_steps}

def style(categories, top_category):
    return f'Categories provided: {categories}\nCategory chosen: {top_category}'
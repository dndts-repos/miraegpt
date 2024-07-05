from miraegpt.chains.writer import recursive_reply_generation
from miraegpt.langgraph.state import GraphState
from miraegpt.libs.utils import write_markdown_file


def reply(state: GraphState):
    """Replying to Question"""
    print("---Generating Response to Question---")
    initial_message = state['initial_message']
    chat_history = state['most_relevent_chat_history']
    num_steps = int(state['num_steps'])
    num_steps += 1

    response = recursive_reply_generation(initial_message, chat_history)
    write_markdown_file(response, "final_response")

    return {"response": response, "num_steps" : num_steps}

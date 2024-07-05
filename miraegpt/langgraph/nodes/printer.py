from miraegpt.langgraph.state import GraphState

def state_printer(state: GraphState):
    """print the state"""
    print("---STATE PRINTER---")
    print(f"Initial Message: {state['initial_message']} \n" )
    print(f"Category: {state['category']} \n")
    print(f"Response: {state['response']} \n")
    print(f"Num Steps: {state['num_steps']} \n")
    return
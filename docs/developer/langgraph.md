# Langgraph
Langgraph make it easy to visual and execute your process using a state machine. 

## Location
```bash
./
└── miraegpt/
    ├── langgraph/
    │   ├── nodes/
    │   │   ├── information_handler.py
    │   │   ├── issue_type_handler.py
    │   │   ├── query_rewrite_handler.py
    │   │   ├── retriever.py
    │   │   ├── summary_handler.py
    │   │   └── unrelated_handler.py
    │   ├── build.py
    │   └── state.py
```

## State
The state of the graph can be represented by 

``` python
class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """
    current_message: str
    issue_type: str
    chat_histories: List[tuple[str, str]] 
    summary: str
    reply: str
    chunks: List[Document]
```

## Overall Graph
![State Machine](../assets/state-machine.png)

1. User will ask their question and together with any chat summary it will be passed to the `Query Rewriter Handler`.
2. `Query Rewriter Handler` will rewrite the user question to fit the context of the conversation with the chat summary provided. The rewritten question will be routed to `Issue Classifier Handler`. 
3. `Issue Classifier Handler` sees the rewritten question and tries to classify the questions type. 
    1. If the question cannot be classified, it will be routed to `Irrevelent Handler` to generate a response. 
    2. If question can be classified, it will be routed to `Retriever` to fetch any relevent documents from the database. Then the question and fetched documents would be routed to `Information Handler` to generate a response.
4. Once a response is generated, it would be routed to the `Summary Handler` which summarizes all existing conversation.
5. Once the conversation is summarized, the state machine would have ended its cycle.    


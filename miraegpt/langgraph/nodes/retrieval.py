# from langchain_core.documents import Document

# from miraegpt.libs.utils import get_chat_histories, write_markdown_file
# from miraegpt.langgraph.state import GraphState
# # from miraegpt.database.chroma import retriever as RETRIEVER

# def retrieve_documents(state: GraphState):
#     print('---Retrieve Documents from Vector Store---')
#     initial_message = state['initial_message']
#     category = state['category']
#     num_steps = state['num_steps']
#     num_steps += 1

#     relevent_documents = RETRIEVER.invoke(initial_message, {'metadata': {"source": category}})

#     chat_histories = get_chat_histories(relevent_documents)

#     write_markdown_file(style(chat_histories), 'chat_history_retrieved')
#     return {"chat_histories": chat_histories, "num_steps": num_steps}

# def style(chat_histories: list[list[Document]]):
#     result = ''
#     for chat_history in chat_histories:
#         for chat in chat_history:
#             sender = chat.metadata['sender']
#             content = chat.page_content
#             result += f'{sender}:\n{content}\n\n'
#         result += f'{'-' * 70}\n'
#     return result

# if __name__ == "__main__":
#     category = "delivery"
#     documents = RETRIEVER.invoke("I did not received my package.", {'metadata': {'source': category}})
#     chat_histories = get_chat_histories(documents)

#     write_markdown_file(style(chat_histories), 'chat_history_retrieved')

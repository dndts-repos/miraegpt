from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from miraegpt.models.llm import LLAMA_LLM

MESSAGE_KEY = "initial_message"
CHAT_HISTORY_KEY = "chat_history"

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a master at crafting email replies. You will be given 2 information,
        1. message - this is the message that you have to reply to
        2. chat history - this is a chat history where the content are similar or relevent to the message you are replying to.

    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Conduct a comprehensive analysis of the message provided and using the context provided by the chat history,
    You are tasked to write a reply to the message. 

    NOTE:
        Personal Information such as name, tracking URL, email, etc provided in chat history SHOULD NOT be used when crafting the reply.
        Your reply should be tailored towards the message provided.

    Provide the output as a form of JSON with a single key "response" and the value is your reply.
    Example:
        "response" : "Please provide your address for us to assist you further."

    DO NOT add any premable or explanation
        
    MESSAGE:\n\n{initial_message}\n\n
    CHAT HISTORY:\n\n{chat_history}\n\n
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[MESSAGE_KEY, CHAT_HISTORY_KEY],
)

reply_generator = prompt | LLAMA_LLM | JsonOutputParser()

def recursive_reply_generation(message, chat_history) -> str:
    try:
        reply = reply_generator.invoke({
            MESSAGE_KEY: message,
            CHAT_HISTORY_KEY: chat_history
        })['response']
        return reply
    except:
        print("Reply Format Invalid! Retrying...")
        return recursive_reply_generation(message, chat_history)

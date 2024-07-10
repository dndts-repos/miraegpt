from langchain.prompts import PromptTemplate
from miraegpt.langgraph.nodes.retriever import retrieve
from miraegpt.langgraph.state import GraphState
from miraegpt.models.llm import GROQ_LLM, LLAMA_LLM
from langchain_core.output_parsers import StrOutputParser


QUESTION_KEY = 'question'
SUMMARY_KEY = 'summary'
DOCUMENTS_KEY = 'documents'

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are an expert at summarizing documents and listing them as steps.
    You are part of a large language model pipeline that would response to a user input with a step-by-step guide.
    You are assisting a company's customer service personel with their daily task. 
    The company is a second hand phone retailer that ships and sells phones in Europe. When the customer received their phones, they may face some difficulties or issues with their phones. 
    The customer service personel's job is to assist the customer in solving their problem with the lowest cost possible.
    As the company is selling phone through a third party platform called BackMarket. As such, BackMarket acts as a middleman between the company and the customer.
    Any user input received are paraphrased by the company's customer service personnel from BackMarket's messages.
    Your task is to reply to the customer service personel's query and solving their problems.
    You will be given
        1. Question - The question that was parapharsed by the customer service personel using BackMarket's message
        2. Summary (if any) - The summary of chat histories between you and the customer service personel.
        3. Documents - Chunks of documents which contain Email Templates prepared by the company to answer the question.
    
    You are required to understand the context through the question provided and guide the customer service personel in answering their question.
    YOU DO NOT NEED TO PROVIDE A SAMPLE RESPONSE. Suppose the customer service did not specify the type of output to provide, provide your answer as a list of steps. Otherwise, reply ONLY in the format specified.

    Suppose the given question and documents are not sufficient for you to provide any form of response, DO NOT INSIST on providing a reply.
    Rather, please inform the customer service personel that the information provided are insufficient or irrelevant and ask them to consult the Company Boss (Boss Daniel) instead.<|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    Question: {question}
    Summary: {summary}
    Documents: 
    {documents}<|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[QUESTION_KEY, SUMMARY_KEY, DOCUMENTS_KEY]
)

INFORMATION_CHAIN = prompt | GROQ_LLM | StrOutputParser()

if __name__ == "__main__":
    question = "The NFC function does not work"
    issue = 'NFC'
    state = GraphState(current_message=question, issue_type=issue)
    documents = retrieve(state)['chunks']
    print(documents)
    print(INFORMATION_CHAIN.invoke({QUESTION_KEY: question, DOCUMENTS_KEY: documents}))
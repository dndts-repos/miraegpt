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
    You are part of a large language model pipeline designed to summarise documents and respond to user input.
    Context:
    You assist a company's customer service personnel with their daily tasks. The company is a second-hand phone retailer in Europe, selling phones through the third-party platform BackMarket, which acts as a middleman between the company and its customers. Customer inquiries are paraphrased from Backmarket messages by the company's customer service personnel.

    Your Task:
    Your job is to response to the customer service personnel's queries and help solve customer problems at the lowest cost possible.
    Your will receive:
        1. Question: The paraphrased question from the customer service personnel.
        2. Summary (if any): A summary of chat histories between you and the customer service personnel.
        3. Documents: Chunks of documents containing email templates prepared by the company to answer the question.
    Instructions:
        1. Understand the context from the question provided.
        2. Guide the customer service personnel in answering their question in the specified format.
        3. If no format specified, provide your answer as general explanation.
        4. If the provided Documents and Summary are insufficient or irrelevant, do not provide a response. Instead, inform the customer service personnel to consult the Company Boss (Boss Daniel) for further information.
    Note: DO NOT RECOMMEND THE RESPONSE FORMAT<|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    Question: {question}
    Summary: 
    {summary}
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
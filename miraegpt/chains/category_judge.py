from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from miraegpt.models.llm import LLAMA_LLM

MESSAGE_KEY = "initial_message"
ISSUES_KEY = "issues"

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a master at understanding message and determine what kind of issue the message is addressing given a list of potential issues.

    <|eot_id|><|start_header_id|>user<|end_header_id|>
    The list below are all possible issues from a given message:
        delivery - used when issues regarding delivery arise \
        screen  - used when issues regarding screen arise \
        sim - used when issues regarding sim card arise \
        battery - used when issues regarding battery arise \
        camera - used when issues regarding camera arise \
        region - used when issues regarding geographical location arise \
        network - used when issues regarding network or connectivity arise \
        accessories - used when issues regarding accessories arise \
        replacement - used when issues regarding returning or replacing phone arise\
        irrelevent - used when NO issues above matches the message

    Conduct a comprehensive analysis of the message provided, 
    Return a JSON with a single key 'category' and no premable or explaination where the value is one of these {issues}.
    example:
        'category' : 'delivery'
    
    DO NOT add any premable or explanation
        
    MESSAGE_CONTENT:\n\n{initial_message}\n\n
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[MESSAGE_KEY, ISSUES_KEY],
)

category_judge_generator = prompt | LLAMA_LLM | JsonOutputParser()

def recursive_judge_invoke(doc, categories):
    if len(categories) == 1:
        return categories[0]
    try:
        category = category_judge_generator.invoke(
            {MESSAGE_KEY: doc, ISSUES_KEY: categories}
        )['category']
        if category not in categories:
            print('retrying...')
            return recursive_judge_invoke(doc, categories)    
    except:
        print('retrying...')
        return recursive_judge_invoke(doc, categories)
    return category
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from miraegpt.models.llm import LLAMA_LLM

COMMA = ','
MESSAGE_KEY = "initial_message"
OUTPUT_KEY = "output_prompt"

SINGLE_OUTPUT_PROMPT = """Output a single category only from the types (delivery, screen, sim, battery, camera, region, network, accessories, replacement)\
            eg:
            delivery
"""

MULITPLE_OUTPUT_PROMPT = """Output one or many relevent categories (separated by comma) from the types (delivery, screen, sim, battery, camera, region, network, accessories, replacement)\
            eg:
            delivery, replacement, accessories
"""

# Need to refactor the type of issues
prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are a Message Categorizer Agent. You are a master at understanding what customer's issue is when they write a message and are able to categorize it in a useful way.

    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Conduct a comprehensive analysis of the message provided and categorize into one of the following issues:
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
            
            {output_prompt}
    
    MESSAGE_CONTENT:\n\n{initial_message}\n\n
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[MESSAGE_KEY, OUTPUT_KEY],
)

message_category_generator = prompt | LLAMA_LLM | StrOutputParser()

def recursive_generator_invoke(doc):
    categories = message_category_generator.invoke(
        {MESSAGE_KEY: doc, OUTPUT_KEY:MULITPLE_OUTPUT_PROMPT}
    ).split(COMMA)
    categories = list(map(lambda x: x.strip(), categories))
    result = sum(list(map(lambda x: len(x.split(' ')), categories)))
    if result != len(categories):
        print('retrying...')
        return recursive_generator_invoke(doc)
    return categories

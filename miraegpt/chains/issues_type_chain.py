from typing import Literal
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables.utils import Input
from langchain_core.exceptions import OutputParserException
from langchain_core.runnables import RunnableLambda

from miraegpt.models.llm import MAX_LLM_RETRIES, TOOL_LLAMA_LLM

QUESTION_KEY = 'question'

class IssueType(BaseModel):
    value: Literal[
        'Region', 
        'Grade', 
        'Pin', 
        'Battery', 
        'Bluetooth', 
        'Charging', 
        'Network', 
        'Speaker', 
        'Camera', 
        'NFC', 
        'Audio', 
        'Screen',
        'Power',
        'SD',
        'Personal',
        'Water',
        'Sim',
        'Rattle',
        'iCloud',
        'Unrelated'
    ] = Field(
        ...,
        description="Given a user question, choose which issues fits the question the best."
    )

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>You are an expert at mapping user question to the type of issue the question is asking.
    You helping a second hand phone retailer with its customer service. Most of the questions provided would be phone related issues. Here are the issues:
        1. Region - Issue about receiving Korean, Japanese or Chinese Phone or phone not suitable for Europe.
        2. Grade - Issue about any grade discrepancies with the phone recieved. Customer may bought a good condition phone but received a poor condition phone.
        3. Pin - Issue with phone being lock and unable to unlock without a password
        4. Battery - Issue with phone battery or phone heating up
        5. Bluetooth - Issue with phone's bluetooth connectivity
        6. Charging - Issue with slow charging or unable to charge
        7. Network - Issue with network connectivity, such as 4G, 5G, Wifi or LTE
        8. Speaker - Issue with phone speaker, might be clogged, fuzzy or sounds soft.
        9. Camera - Issue with phone camera, like taking a picture
        10. NFC - Issue with phone's NFC
        11. Audio - Issue with audio jack or microphone, like audio jack not functional or people could not hear each other through call
        12. Screen - Issue with phone screen, like touch screen not working
        13. Power - Phone unable to turn on or power on
        14. SD - Issue with phone's SD card reader
        15. Personal - Issue with phone is caused by customer not us, like dropping phone on the floor
        16. Water - Phone got water damaged
        17. Sim - Issue with sim card or dual sim or e-sim
        18. Rattle - Phone makes rattling noise when shake
        19. iCloud - Issue with iCloud
        20. Unrelated - Used when none of the other issues can match<|eot_id|>
        <|start_header_id|>user<|end_header_id|>
        Question: {question} <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
    """,
    input_variables=[QUESTION_KEY]
)

'''
In the event where the LLM is unable to provide a response,
which maybe due to some OutputParserException or ValueError,
the Issue Type would be defaulted to 'Unrelated'.
'''
def issue_type_fallback(inputs: Input):
    print('----- Issue Type Chain: Invoking Fallback -----')
    return IssueType(value='Unrelated')

ISSUE_TYPE_LLM = TOOL_LLAMA_LLM\
    .with_structured_output(IssueType)\
    .with_retry(retry_if_exception_type=(OutputParserException, ValueError), stop_after_attempt=MAX_LLM_RETRIES)\
    .with_fallbacks([RunnableLambda(issue_type_fallback)])

ISSUE_TYPE_CHAIN = prompt | ISSUE_TYPE_LLM
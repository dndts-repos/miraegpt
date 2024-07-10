from typing import Literal
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables.utils import Input
from langchain_core.exceptions import OutputParserException
from langchain_core.runnables import RunnableLambda

from miraegpt.models.llm import GROQ_LLM, MAX_LLM_RETRIES, TOOL_LLAMA_LLM

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
        'Accessories',
        'Lost',
        'Withdraw',
        'Address',
        'Chronopost',
        'Stuck',
        'No Stock',
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
        20. Accessories - Issue with Phone Case, Protector, Charging Cable, Charger, Plug or Earphone/Earpiece
        21. Lost - Issue with delivery, phone went missing or parcel is lost or wrong item received or parcel is delivered but customer did not receive.
        22. Withdraw - Issue with customer withdrawing their purchase
        23. Address - Issues with delivery when customer changes address
        24. Chronopost - Issues regarding Chronopost point.
        25. Stuck - Issues with delivery when parcel is stuck in transit
        26. No Stock - Issue when item is out of stock
        27. Unrelated - Used when none of the other issues can match<|eot_id|>
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

ISSUE_TYPE_LLM = GROQ_LLM\
    .with_structured_output(IssueType)\
    .with_retry(retry_if_exception_type=(OutputParserException, ValueError), stop_after_attempt=MAX_LLM_RETRIES)\
    .with_fallbacks([RunnableLambda(issue_type_fallback)])

ISSUE_TYPE_CHAIN = prompt | ISSUE_TYPE_LLM

if __name__ == '__main__':
    qa = {
        'My phone is in Korean' : 'Region',
        'My phone is not suited for europe' : 'Region',
        'I bought a Very Good Condition phone but the phone\'s condition is no where near very good' : 'Grade',
        'My device came with a PIN code. I do not have the code' : 'Pin',
        'My phone is locked. I do not have the password': 'Pin',
        'The phone battery health is only 70%': 'Battery',
        'The battery health is in a bad state': 'Battery',
        'My phone discharges in 1 hour': 'Battery',
        'My phone only can last 1 hour': 'Battery',
        'My device cannot connect to bluetooth': 'Bluetooth',
        'My phone is not charging': 'Charging',
        'My phone takes a long time to charge': 'Charging',
        'My phone cannot receive network when making call': 'Network',
        'My phone\'s mobile data is very weak': 'Network',
        'The speaker is clogged': 'Speaker',
        'My phone makes a sound when taking picture even though it is silent': 'Camera',
        'The NFC function does not work': 'NFC',
        'The audio jack is not working' : 'Audio',
        'My phone cannot turn on': 'Power',
        'The touch screen on the phone is not working': 'Screen',
        'There is green bar on my phone screen': 'Screen',
        'People cannot hear me when I make a call' : 'Audio',
        'The SD card is not working': 'SD',
        'I dropped my phone and now it is broken': 'Personal',
        'The camera has a black spot': 'Camera',
        'My phone got water damaged': 'Water',
        'My phone is preloaded with Chinese applications': 'Region',
        'My device is showing me LTE instead of 4G/5G.': 'Network',
        'My phone does not have a dual sim': 'Sim',
        'The battery in my phone is not real': 'Battery',
        'When I shake my phone, I can hear something loose inside': 'Rattle',
        'How do I remove iCloud lock remotely': 'iCloud',
        'My device does not recognise my sim card': 'Sim',
        'My package came empty.' : 'Lost',
        'My package is lost' : 'Lost',
        'Tracking link said delivered but customer did not receive it': 'Lost',
        'Customer return device to us but parcel lost': 'Lost',
        'I would like to withdraw': 'Withdraw',
        'Customer would like to change their address': 'Address',
        'Customer could not find the pin to retrieve their product from the chronopost point': 'Chronopost',
        'Parcel stuck in transit': 'Stuck',
        'Stock is out of order' : 'No Stock',
        'I did not receive the case and screen protector indicated during the order purchase': 'Accessories',
        'The cable is not working properly': 'Accessories',
        'The charger is not working properly': 'Accessories',
        'The order does not come with earphones': 'Accessories',
        'Today is a nice day': 'Unrelated',
        'Ba Ba Black sheep': 'Unrelated',
        'My phone has a dinosaur': 'Unrelated'
    }

    count = 0
    total = len(qa)
    invalids = []
    for question, answer in qa.items():
        response: IssueType = ISSUE_TYPE_CHAIN.invoke({QUESTION_KEY: question})
        response_type = response.value
        print(f'Question: {question}')
        print(f'Actual: {answer}')
        print(f'Predict: {response_type}')
        if answer == response_type:
            count += 1
        else:
            invalids.append((question, answer, response_type))
    
    print(f'Score: {count}/{total}')

    for invalid in invalids:
        print(invalid)
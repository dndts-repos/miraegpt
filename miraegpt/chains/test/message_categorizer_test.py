import os
from src.chains.message_categorizer import (
    message_category_generator as GENERATOR, 
    MESSAGE_KEY,
    OUTPUT_KEY,
    SINGLE_OUTPUT_PROMPT
)

READ_PATH = os.path.join('src', 'chains', 'test')
COMMA = ','

def is_equal(pred, actual):
    if pred == actual:
        return True, "Actual matches Prediction"
    return False, "Actual does not match Prediction"

def test_simple_message():
    filename = 'short_message.txt'
    q_and_a = []
    score = 0
    with open(os.path.join(READ_PATH, filename), 'r') as file:
        for line in file.readlines():
            q_and_a.append(list(map(lambda x: x.strip(), line.split(COMMA))))
    for question, answer in q_and_a:
        pred = GENERATOR.invoke({MESSAGE_KEY: question, OUTPUT_KEY: SINGLE_OUTPUT_PROMPT}).strip(' \n\'"')
        res, message = is_equal(pred, answer)
        if res:
            score += 1
        print(message)
        print(f"actual: {answer} | prediction: {pred}")
    print(f"Results: {score}/{len(q_and_a)}")

VALID_LONG_MESSAGE_FILENAMES = set(["S00" + str(i) + "_message.txt" for i in range(1, 9)])

def validate_long_message_filename(filename):
    return filename in VALID_LONG_MESSAGE_FILENAMES

def test_long_message():
    filenames = list(filter(validate_long_message_filename, os.listdir(READ_PATH)))
    q_and_a = []
    score = 0
    for filename in filenames:
        with open(os.path.join(READ_PATH, filename), 'r') as file:
            content = file.readlines()
            answer = content[-1]
            question = '\n'.join(content[:-1])
            q_and_a.append([question, answer])
    for question, answer in q_and_a:
        pred = GENERATOR.invoke({MESSAGE_KEY: question, OUTPUT_KEY: SINGLE_OUTPUT_PROMPT}).strip(' \n\'"')
        res, message = is_equal(pred, answer)
        if res:
            score += 1
        print(message)
        print(f"actual: {answer} | prediction: {pred}")
    print(f"Results: {score}/{len(q_and_a)}")

test_long_message()
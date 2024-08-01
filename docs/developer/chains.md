# Chains

## Location
```bash
./
└── miraegpt/
    ├── chains/
    │   ├── information_chain.py
    │   ├── issues_type_chain.py
    │   ├── query_rewrite_chain.py
    │   ├── summary_chain.py
    │   └── unrelated_chain.py
```

## Description
All chains are built using the `langchain` framework. Chains are essentially a sequence of pipe operations where the output of a previous process becomes the input of the next process. 

### Information Chain
**Prompt**    
The model will be given the initial question, summary of the chat history and some retrieved documents from the vector database. Then using these information, the model will piece a reply to the initial question. 

**Chain**  
Initial Question, summary and documents will be passed into the prompt template, then the prompt will be piped into the model. Once the model completed its process, it will pipe its output to StrOutputParser which will parse the output into a string. 

### Issues Type Chain
**Prompt**    
The model will be given the initial question and it need to categorise the question into one of the following, 
```python
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
```

**Chain**  
Initial Question will be passed into the prompt template, then the prompt would be piped into a model with structured output. The output will look something like: 
> {'value': 'Battery'}

Note that this structured model might fail to parse its output as the structure we want. As such, it will raise either an `OutputParserException` or a `ValueError`.   
The model is configured such that it will retry at most `MAX_LLM_RETRIES` times before activating a fallback which would just classify the question as `Unrelated`.

### Query Rewrite Chain
**Prompt**    
Initial Question and a summary of the chat history will be provided. Using these information, the model is suppose to come up with a paraphrased question that would incorporate the initial question and the summary to form a question that is more cohesive to the chat context. 

**Chain**  
Initial Question and summary of the chat history is provided to the prompt template. Then the prompt would be piped into the model. The output of the model will be parsed into a string using `StrOutputParser`. 

### Summary Chain
**Prompt**    
Chat history (last 3 conversation between user and miraeGPT) and summary (summary of the entire conversation between user and miraeGPT) will be provided to the model. Using these information, the model would attempt to summarize the entire conversation that the user had with miraeGPT. 

**Chain**  
Chat history and summary is provided to the prompt template, then the prompt is piped into the model. The output of the model will be parsed into a string using `StrOutputParser`

### Unrelated Chain
**Prompt**    
Given the user question and summary, the model would come up with a response telling the user that it has limited knowledge to help the user regarding the given question. 

**Chain**  
User question and summary are provided to the prompt template, then the prompt is piped into the model. The output of the model will be parsed into a string using `StrOutputParser`.


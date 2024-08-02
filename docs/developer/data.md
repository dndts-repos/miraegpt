# Data

## Location
```bash
./
└── miraegpt/
    ├── data/
    │   ├── chat_history
    │   ├── chroma
    │   └── templates/
    │   │   ├── accessories
    │   │   ├── delivery
    │   │   └── technical
```

## Description
1. Chat History
    - Chat history is not in used currently.
    - These are chat history that is retrieved from the Backmarket SAVs using Backmarket's API. 
    - It is not in used due to the inconsistency of answers on similar questions.
2. Chroma
    - This is the vector database.
    - As Chroma is built on top of sqlite, it also adopts a file based approached. Meaning the data are saved and read as a file rather then having a server set up. 
    - DO NOT mess with this file unnecessary as it contains all the vectorised documents that the model used to retrieve any relevant documents. 
3. Templates
    - These are templates taken from the [ecomms notes](https://docs.google.com/document/d/1s1b0FkAROP_YMSLDiVSGTnAVqHMvGcpvR7EX9XFqEvg/edit?usp=sharing) page 19 to 54.
    - These are also the templates that are vectorised and stored in the vector database.
    - The templates are also categorized into `accessories`, `delivery` and `technical`. Hence, when adding the any new templates, please classify them under their respective categories.  
    - **NOTE: template naming convention is** `<template id><WHITESPACE><issue type>.docx`
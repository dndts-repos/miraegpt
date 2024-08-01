# Backend

## Prerequisites
This section of backend cover both the backend and miraegpt components shown in [Overall Architecture](../developer/overall-architecture.md). As such, developers should have some knowledge about the following concept and technologies used:  

1. FastAPI  
2. LangServe  
3. LangChain  
4. LangGraph  
5. Chromadb  
6. Docker

Please read up on these technologies by looking through their official documentations or online tutorial before you try to develop.  


## Folder Structure
```bash
./
└── miraegpt/
    ├── backend/
    │   └── serve.py
    ├── chains/
    │   ├── information_chain.py
    │   ├── issues_type_chain.py
    │   ├── query_rewrite_chain.py
    │   ├── summary_chain.py
    │   └── unrelated_chain.py
    ├── data/
    │   ├── chat_history
    │   ├── chroma
    │   └── templates
    ├── database/
    │   └── chroma.py
    ├── langgraph/
    │   ├── nodes/
    │   │   ├── information_handler.py
    │   │   ├── issue_type_handler.py
    │   │   ├── query_rewrite_handler.py
    │   │   ├── retriever.py
    │   │   ├── summary_handler.py
    │   │   └── unrelated_handler.py
    │   ├── build.py
    │   └── state.py
    ├── libs/
    │   ├── loader.py
    │   └── utils.py
    ├── models/
    │   └── llm.py
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

## Set up
### Without Docker
1. In the `backend` folder, there should be a `requirements.txt` file. Run the following command:
> pip install requirements.txt
2. Go to [Ollama](https://ollama.com), follow its installation guide
    1. Then install the embbedder [`mxbai-embed-large`](https://ollama.com/library/mxbai-embed-large)
3. Go to [groq](https://groq.com/) and get the API key.
4. Set up `.env` file in `..` folder and add the key `GROQ_API_KEY` with groq API key as value.
5. Then in `backend` folder, run  
> python main.py

### With Docker
1. Go to [Ollama](https://ollama.com), follow its installation guide
    1. Then install the embbedder [`mxbai-embed-large`](https://ollama.com/library/mxbai-embed-large)
2. Go to [groq](https://groq.com/) and get the API key.
3. Set up `.env` file in `..` folder and add the key `GROQ_API_KEY` with groq API key as value.
4. Build the Docker Image with name `miraegpt-server` and run the image as container.


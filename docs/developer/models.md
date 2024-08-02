# Models

## Location
```bash
./
└── miraegpt/
    ├── models/
    │   └── llm.py
```

## Description
The chatbot uses `llama3` model from `groq` and `mxbai-embed-large` model from `ollama`. 

- For `llama3`, ensure you have the groq API key in your `.env` file. 
- For `ollama`, ensure you have the embedder model in your local machine.
- For `ollama`, 
    - if you are using docker, ensure the ollama URL is specified in `Dockerfile` or `docker-compose.yml`. 
    - If you are using local machine, just make sure the local ollama server is running on port `11434`.
# Server

## Location
```bash
./
└── miraegpt/
    ├── backend/
    │   └── serve.py
```

## Description
1. It creates a FastAPI instance and store it as `app`. 
2. Afterwhich, we use the `add_routes` function in `Langserve` to add the path `/gpt` for our chatbot with the `miraegpt` runnable from `miraegpt.langgraph.build`.

With the steps above, we tap on `Langserve`'s function to help us create different endpoints like `/invoke`, `/stream` etc that can be call by any client. 

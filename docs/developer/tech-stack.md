# Tech Stack
MiraeGPT is primarily built using `python` with its various libraries/packages and using `llama3` as the LLM. Here are the different technologies used:

- Frontend: [Streamlit](https://docs.streamlit.io/develop/tutorials/llms)
    - Streamlit makes it easy to simple up a chat interface fast with its prebuild components and memory-managment. 
- Backend: [FastAPI](https://fastapi.tiangolo.com/), [Langserve](https://python.langchain.com/v0.1/docs/langserve/)
    - Langserve, provided by the Langchain team, make it possible to turn the LLM into a RESTful API with just one line and provides a variety of endpoints to interact with the LLM. 
    - FastAPI is the underlying backend framework used by Langserve. 
- Database: [Chroma](https://docs.trychroma.com/)
    - Chroma is a open-sourced vector database where it enable documents to be saved as vectors. 
    - It is built using sqlite which means it is a file-based database as compared to being a server-based database like MySQL or Postgres.
- LLM Framework: [Langchain](https://python.langchain.com/v0.2/docs/introduction/),  [Langgraph](https://langchain-ai.github.io/langgraph/how-tos/)
    - Langchain provide wrappers around other useful tools like reading, chunking, retrieving documents.
    - Langgraph make it easier to develop and visualise application through the use of graphs.  
- LLM: [Ollama](https://www.ollama.com/), [Groq](https://groq.com/)
    - Ollama allows us to running LLM locally. However, because it is running locally, the speed of the model is limited by the hardware resources available. 
    - Groq is a Cloud LLM service that allows us to running our queries using their LLM. With Groq, we are able to run a powerful and resource intensive models without compromising speed.
- Deployment: [Docker](https://docs.docker.com/), [ngrok](https://ngrok.com/docs/)
    - MiraeGPT is built using microservice architecture and Docker is used to containerize the services.
    - ngrok is used to deploy the application, providing a tunnel so that client can used MiraeGPT from anywhere.
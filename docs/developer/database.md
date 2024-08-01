# Database

## Location
```bash
./
└── miraegpt/
    ├── database/
    │   └── chroma.py
```

## Description

![Data Processing Process](../assets/data-processing-process.png)

As seen from the diagram above,  

1. Templates are saved in `data/templates`.  
2. Using `load_word_documents`, we load the word documents.  
    - Here, we used the package `unstructured` to help us with the loader.  
    - Every template will be loaded with 2 attributes,`page_content` and `metadata`.   
    - In `metadata`, we would also include other useful information like `source` which is the filename of the template and also `issue_type` which we can get from the [name of the template](../developer/data.md#description). 
3. Then using `chunk_documents`, the documents from step 2 will be recursively chunked into smaller byte size.
    - The chunk id will also be added as part of the metadata

4. Subsequently, the chunks will be written into the vectorstore using `write_to_vectorstore`. 
    - Note that we are using the embedder `mxbai-embed-large` from the local Ollama. So do ensure that Ollama server is running locally and the embedder is pulled to your local machine.
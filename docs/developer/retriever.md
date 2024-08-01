# Retriever Handler

This handler's role is to retrieve relevant documents based on the state's `current_message` and `issue_type`.

It will

 1. Get `current_message` and `issue_type` from the state. 
 2. Connect to the vectorstore/vectordb. 
 3. Perform a similarity search on the vectordb with `current_message` and filtered by `issue_type` to retrieve relevant documents.
 4. Update state's `chunks` attributes with the documents retrieved.
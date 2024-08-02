# Information Handler

This handler's role is to use most of the information provided by state to form a constructive response for the user's question. 

## Procedure
1. Get `current_message`, `chunks`, `summary` and `chat_histories` from the state. 
2. For all the chunks provided, concatenate all `page_content` into a single string. 
3. Invoke the [`information chain`](../developer/chains.md#information-chain) and get a response back.
4. Get the 3 most recent chat histories. 
5. Update the state's `reply` with the response from step 3 and `chat_histories` with the chat histories from step 4. 
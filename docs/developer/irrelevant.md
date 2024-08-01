# Irrelevant/Unrelated Handler

This handler's role is to construct a response back to the user when the user provides a question that is unrelevant. 

## Procedure
1. Get `current_message` and `summary` from the state. 
2. Invoke [`unrelated chain`](../developer/chains.md#unrelated-chain)
to generate a response.
3. Get chat histories with the last 3 conversation between user and bot.
4. Update the state's `reply` with response from step 2 and state's `chat_histories` attributes with the chat histories from step 3.
# Summary Handler

This handler's role is to provide a summary based on the entire conversation with the main focus of the summary being the last 3 conversation between the user and the model. 

## Procedure
1. Get `chat_histories` and `summary` from the state.
2. Invoke [`summary chain`](../developer/chains.md#summary-chain) to get the summarised conversation.
3. Replace the `summary` attribute from state with the new summarised conversation from step 2. 
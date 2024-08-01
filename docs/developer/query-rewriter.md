# Query Rewriter Handler
This handler job is to help the user rewrite their question to fit the context of the conversation better. 

## Procedure
1. Get `current_message` and `summary` from the state.
2. Invoke [`Query Rewrite Chain`](../developer/chains.md#query-rewrite-chain) to get a rewritten question.
3. Replace `current_message` attribute from the state with the rewritten question. 
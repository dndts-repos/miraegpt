# Issues Classifier Handler

This handler's role is to determine the issue type based on the given question. 

## Procedure
1. If the state already has an `issue_type`, the handler will continue to use the same `issue_type`.
2. Otherwise, it will get `current_message` from the state.
3. Invoke [`issue type chain`](../developer/chains.md#issues-type-chain) and get the issue type
4. Update the state's `issue_type` with the value from step 3.

# jira-ingest

Turns raw Jira tickets into documents ready to be embedded for the Ask Engineering assistant.

```
pip install pytest
pytest -v
```

## Your task (20 min)

Please think out loud throughout.

| Step | What to do | Time |
|---|---|---|
| 1 | Read the repo and explain what it does in your own words | 3 min |
| 2 | Describe how you would restructure it, and what a full ingestion pipeline would need. Add placeholder functions only, no implementation | 4 min |
| 3 | Run the tests and explain why each failing test fails | 2 min |
| 4 | Fix the failing tests and implement `ticket_to_documents()` in `main.py` | 10 min |
| 5 | Walk us through your changes | 1 min |

## Using AI

Using AI is your choice. It is neither required nor penalised. We score how you use it.

- Write `ticket_to_documents()` yourself, without AI.
- Before each prompt, tell us what you are about to ask and why.
- Ask about one specific thing: one function, one error, or one fix you have already described.
- Do not go straight to having the AI implement a change. First read its suggestion and explain
  what it will change. Only then apply it.
- You must be able to explain every line the AI writes.

Not allowed, and marked as a fail:
- Pasting multiple files or the whole repo into the AI.
- Prompts like "fix the failing tests" or any other one-shot request to solve the task.
- Applying AI output you have not read and explained.

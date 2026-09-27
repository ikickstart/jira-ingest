import json
from helpers import clean_text

DATA_PATH = "data/issues.json"


def load_issues(path):
    with open(path) as f:
        return json.load(f)["issues"]


def format_comment(comment):
    return f"{comment['author']['displayName']}: {clean_text(comment['body'])}"


def get_permission(ticket):
    # security level restricts who can see the ticket
    return ticket["fields"]["security"]["name"]


def ticket_to_documents(ticket: dict) -> list[dict]:
    """
    Split one Jira ticket into documents for indexing.

    - One document for the description, if it is not empty.
      Text is the cleaned description.
    - One document per comment, if the comment body is not empty.
      Text comes from format_comment().
    """
    documents = []
    # TODO
    return documents


def run():
    issues = load_issues(DATA_PATH)
    all_docs = []
    for ticket in issues:
        for doc in ticket_to_documents(ticket):
            doc["permission"] = get_permission(ticket)
            all_docs.append(doc)
    print(f"Built {len(all_docs)} documents")
    return all_docs


if __name__ == "__main__":
    run()

import re


def clean_text(text):
    """Strip Jira markup and collapse whitespace."""
    if not text:
        return ""
    text = re.sub(r"\{code[^}]*\}", "", text)
    text = re.sub(r"[*_\[\]]", "", text)
    return " ".join(text.split())

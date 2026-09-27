from main import load_issues, format_comment, get_permission, ticket_to_documents

ISSUES = {t["key"]: t for t in load_issues("data/issues.json")}


def test_load_issues():
    assert len(ISSUES) == 5


def test_format_comment_strips_markup():
    comment = {"author": {"displayName": "Tom Whitfield"},
               "body": "*Fixed.* Raised the timeout in {code}deploy/migrate.sh{code}"}
    assert format_comment(comment) == "Tom Whitfield: Fixed. Raised the timeout in deploy/migrate.sh"


def test_format_comment_keeps_identifiers():
    comment = {"author": {"displayName": "Tom Whitfield"},
               "body": "ALTER TABLE on checkout_orders takes  ~45s"}
    assert format_comment(comment) == "Tom Whitfield: ALTER TABLE on checkout_orders takes ~45s"


def test_permission_uses_security_level():
    assert get_permission(ISSUES["PAY-877"]) == "payments-restricted"


def test_permission_defaults_to_project():
    assert get_permission(ISSUES["PLAT-2291"]) == "project:PLAT"


def test_documents_for_ticket_with_comments():
    docs = ticket_to_documents(ISSUES["PLAT-2291"])
    assert len(docs) == 9
    assert docs[0]["id"] == "PLAT-2291#desc"
    assert docs[1]["id"] == "PLAT-2291#c31001"
    assert docs[1]["text"] == "Tom Whitfield: Looking at it."


def test_skips_empty_comments():
    docs = ticket_to_documents(ISSUES["PLAT-2310"])
    assert [d["id"] for d in docs] == ["PLAT-2310#desc", "PLAT-2310#c31020"]


def test_empty_ticket_has_no_documents():
    assert ticket_to_documents(ISSUES["PAY-901"]) == []


def test_document_url():
    docs = ticket_to_documents(ISSUES["PAY-877"])
    assert len(docs) == 4
    assert all(d["url"] == "https://acme.atlassian.net/browse/PAY-877" for d in docs)

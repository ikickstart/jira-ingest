import json
import urllib.request

JIRA_BASE_URL = "https://acme.atlassian.net"
JIRA_API_TOKEN = "jira-token-hardcoded-123"


class JiraClient:
    def __init__(self):
        self.base_url = JIRA_BASE_URL
        self.token = JIRA_API_TOKEN

    def get_issue(self, key):
        req = urllib.request.Request(
            f"{self.base_url}/rest/api/3/issue/{key}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)

    def load_from_file(self, path):
        with open(path) as f:
            return json.load(f)["issues"]

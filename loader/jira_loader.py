import httpx
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_jira_tickets(jql="project = YOURPROJECT"):
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/2/search"
    auth = (os.getenv("ATLASSIAN_EMAIL"), os.getenv("ATLASSIAN_API_TOKEN"))
    params = {"jql": jql, "maxResults": 50}
    response = httpx.get(url, auth=auth, params=params)
    issues = response.json().get("issues", [])
    return [
        {
            "title": issue["fields"]["summary"],
            "content": issue["fields"]["description"] or "",
        }
        for issue in issues
    ]

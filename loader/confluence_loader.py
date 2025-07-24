import httpx
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_confluence_pages():
    url = f"{os.getenv('CONFLUENCE_BASE_URL')}/rest/api/content"
    auth = (os.getenv("ATLASSIAN_EMAIL"), os.getenv("ATLASSIAN_API_TOKEN"))
    print(auth, url)
    all_pages = []
    start = 0

    while True:
        params = {"start": start, "limit": 25, "expand": "body.storage"}
        response = httpx.get(url, auth=auth, params=params)
        print(response.status_code)
        data = response.json()
        for result in data.get("results", []):
            content = result["body"]["storage"]["value"]
            title = result["title"]
            all_pages.append({"title": title, "content": content})
        if not data.get("_links", {}).get("next"):
            break
        start += 25
    return all_pages

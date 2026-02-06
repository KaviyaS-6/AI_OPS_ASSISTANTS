import requests
import os

def create_repo(repo_name):

    token = os.getenv("GITHUB_TOKEN")

    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "name": repo_name,
        "private": False
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

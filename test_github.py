import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

print("TOKEN FOUND:", token is not None)

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get("https://api.github.com/user", headers=headers)

print("STATUS CODE:", response.status_code)
print("RESPONSE:", response.text)

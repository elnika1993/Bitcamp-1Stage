import sys
import requests
import json

username = sys.argv[1]

response = requests.get(f"https://api.github.com/users/{username}")
print(json.dumps(response.json(), indent=2))
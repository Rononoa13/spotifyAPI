import requests
from config import access_token
import json


header = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get("https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5", headers=header)
print(response)
print(json.dumps(response.json(), indent=3))
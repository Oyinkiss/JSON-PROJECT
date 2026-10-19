import requests
import json
url="https://books.toscrape.com/"
response=requests.get(url, timeout=15)
response.raise_for_status()
try:
  data=response.json()
  print(data["book"])
except json.JSONDecodeError as error:
  print("Invalid JSON", error)

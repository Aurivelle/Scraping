import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/Twitter"
response = requests.get(url)

print(response.status_code)
print(response.text[:500])

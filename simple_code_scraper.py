import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=0wCUAhGr_VQ"

response = requests.get(url)


if response.status_code == 200:
    print("Success")
else:
    print("Failed", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")

print("Title:", soup.title.text)
print("\nLinks: ")
links = soup.find_all("a")
for link in links:
    href = print(link.get("href"))
    if href:
        print(href)

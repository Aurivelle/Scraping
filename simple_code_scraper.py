import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.youtube.com/watch?v=0wCUAhGr_VQ"

response = requests.get(url)


if response.status_code == 200:
    print("Success")
else:
    print("Failed", response.status_code)
    exit()
soup = BeautifulSoup(response.text, "html.parser")

print("Title:", soup.title.text)
unique_links = set()
print("\nLinks: ")
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href:
        full_url = urljoin(url, href)
        unique_links.add(full_url)
output_files = "scraped_links.txt"
with open(output_files, "w", encoding="utf-8") as file:
    file.write("Title: " + soup.title.text + "\n\n")
    file.write("Links: \n")
    for link in unique_links:
        file.write(link + "\n")
print("Links saved in", output_files)

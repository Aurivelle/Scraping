import requests
import time
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random}

url = "https://books.toscrape.com/"


for page in range(1, 6):
    page_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    time.sleep(random.uniform(2, 5))
    response = requests.get(page_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("h3")

        for book in books:
            title = book.a["title"]
            print(title)
    else:
        print("Failed", response.status_code)

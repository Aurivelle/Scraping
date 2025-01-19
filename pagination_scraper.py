import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://quotes.toscrape.com/page/"
headers = {"User-Agent": "Mozilla/5.0"}
pages_to_scrape = 5
output_file = "quotes.csv"
quotes = []

for page in range(1, pages_to_scrape + 1):
    url = base_url + str(page) + "/"
    print("Scraping" + str(page) + ":" + url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        for quote in quote_elements:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            quotes.append([text, author])
    else:
        print("Failed to scrape page", page)
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(quotes)
print("Finished scraping in", output_file)

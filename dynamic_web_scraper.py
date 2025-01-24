from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
url = "https://quotes.toscrape.com/js/"
driver.get(url)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")

quotes = soup.find_all("div", class_="quote")
extracted_data = []

for quote in quotes:
    text = quote.find("span", class_="text").text.strip()
    author = quote.find("small", class_="author").text.strip()
    extracted_data.append([text, author])
    print(f"Quote: {text} - Author: {author}")
output_file = "dynamic_quotes.csv"
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(extracted_data)
driver.quit()
print(f"Data extracted and saved to {output_file}")

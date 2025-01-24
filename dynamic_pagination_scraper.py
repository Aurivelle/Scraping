from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
url = "https://quotes.toscrape.com/js/"
driver.get(url)

extracted_data = []

while True:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "quote"))
    )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        extracted_data.append([text, author])
        print(f"Quote: {text} - Author: {author}")
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Next"))
        )
        next_button.click()
    except:
        print("No more pages to scrape")
        break
output_file = "all_quotes.csv"
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(extracted_data)

driver.quit()
print(f"Data extracted and saved to {output_file}")

import requests
from bs4 import BeautifulSoup
import csv

# Website we want to scrape
BASE_URL = "https://books.toscrape.com/"

# Pretend to be a normal browser (so site doesn’t block us)
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_page(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")

    books = []

    # Each book is inside an <article> tag
    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return books

def main():
    all_books = []
    url = BASE_URL

    # Scrape first 2 pages (you can increase later)
    for page in range(1, 3):
        if page == 1:
            page_url = url
        else:
            page_url = f"{BASE_URL}catalogue/page-{page}.html"

        print(f"Scraping: {page_url}")
        books = scrape_page(page_url)
        all_books.extend(books)

    # Save data into CSV
    with open("books_raw.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "availability"])
        writer.writeheader()
        writer.writerows(all_books)

    print(f"Saved {len(all_books)} books to books_raw.csv")

if __name__ == "__main__":
    main()

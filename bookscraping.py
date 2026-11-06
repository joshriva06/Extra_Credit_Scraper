#!/usr/bin/env python3

import requests
import re
import sys
import concurrent.futures

# Scrape URL for all titles and prices
def scrape(url: str) -> list[tuple]:
    response = requests.get(url)
    text = response.text
    
    titles = re.findall(r'title="([^"]+)"', text) # Find all titles
    prices = re.findall(r'class="price_color">[^\d]*([\d.]+)</p>', text) # Find all prices directly after titles

    books = []
    for title, price in zip(titles, prices): # Compacting our titles and prices into one iterable 
        books.append((title, float(price))) # List of tuples

    return books

def main():
    starter_url = "https://books.toscrape.com/catalogue/page-{}.html"
    pages = [starter_url.format(i) for i in range(1, 51)] # Want to go through multiple web pages

    print('Concurrent Scraping of Top 10 Cheapest Books...')
    
    all_books = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(scrape, pages)

        for result in results:
            all_books.extend(result) # Flatten to single list of tuples, not list of lists

    all_books.sort(key=lambda b: b[1]) # Second element in tuple is price, which is what we sort by

    print("Top 10 Cheapest Books:")
    for index, (title, price) in enumerate(all_books[:10], 1):
        print(f'{index}. {title} - {price}')

if __name__ == '__main__':
    main()

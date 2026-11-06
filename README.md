# 02-B Extra Credit Web Scraper
Python web scraper that scrapes all 50 pages of https://books.toscrape.com/ for the 10 cheapest books

# How to Use
1. Clone repo to your machine
2. Make the script executable with chmod +x bookscraping.py
3. Run with ./bookscraping.py (no command line arguments)

# Performance Impact of Functional Programming and Concurrent Futures
By making 8 workers send HTTP requests to the server at once, we solve the problem of having to wait for each request before starting another one (1 thread pool can only send 1 request at a time). We also apply our scrape() function to our 50 webpages very efficiently using a map function, rather than having to apply it 1 page at a time. 

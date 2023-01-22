# imports requests, imports beautiful soup
import requests
from bs4 import BeautifulSoup

# creates a variable called "page to scrape" and gets the URL and parses HTML
page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# <span class="text" itemprop="text">text</span>
quotes = soup.findAll("span", attrs={"class":"text"})

# <small class="author" itemprop="author">Albert Einstein</small>
authors = soup.findAll("small", attrs={"class":"author"})

# creates a loop, printing quote 
for quote, author in zip (quotes, authors):
    print(quote.text + " - " + author.text)


    
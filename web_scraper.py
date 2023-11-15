import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a.attrs['title']
    rating = book.p.attrs['class'][1]
    price = book.select('.price_color')[0].get_text()
    print(f'Title: {title} | Rating: {rating} | Price: {price}')
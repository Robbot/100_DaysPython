from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

ycwebpage = response.text

soup = BeautifulSoup(ycwebpage, "html.parser")
article_tag = soup.find(name="span", class_="titleline")

print(article_tag)
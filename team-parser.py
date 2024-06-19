import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to parse
url = "https://dota2.fandom.com/ru/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D0%B5_%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B"

# Fetch the content from the URL
response = requests.get(url)

src = response.content

# Parse the content with BeautifulSoup
soup = BeautifulSoup(src, 'lxml')

# Extract and print the title of the page
# title = soup.title
# print(title)

page_all_href = soup.find_all('a')

print(page_all_href)

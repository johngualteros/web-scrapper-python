import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
print(f'{soup.prettify()}')

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

transcript = box.find('div', class_='full-script').get_text(strip = True, separator = ' ')

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)

from bs4 import  BeautifulSoup
import requests

website ='https://subslikescript.com/series/Vikings-2306299/season-5/episode-20-Ragnarok'

response = requests.get(website)

soup = BeautifulSoup(response.text, 'lxml')

box = soup.find('article', class_='main-article')

title = box.find('h1').get_text()

transcript = box.find('div', class_='full-script').get_text('\n', strip=True)

with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
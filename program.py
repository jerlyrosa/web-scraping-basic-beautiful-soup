import requests
from bs4 import  BeautifulSoup

website ='https://subslikescript.com/series/Vikings-2306299/season-5/episode-20-Ragnarok'

response = requests.get(website)
content = response.text


soup = BeautifulSoup(content, 'lxml')


box = soup.find('article', class_='main-article')

title = soup.find('h1').get_text()

transcript = soup.find('div', class_='full-script').get_text('\n', strip=True)

print(transcript)


with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
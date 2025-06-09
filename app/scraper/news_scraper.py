import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    for item in soup.select('.article'):
        title = item.select_one('h2').get_text(strip=True)
        link = item.select_one('a')['href']
        articles.append({'title': title, 'link': link})

    return articles

import requests
import bs4
from datetime import datetime

url = 'https://habr.com/ru/all/'
page = requests.get(url).text
like_hubs = {'JavaScript', 'Python'}
soup = bs4.BeautifulSoup(page, features='html.parser')

articles = soup.find_all(class_="tm-articles-list__item")
for article in articles:
    title = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
    href = url + article.find(class_="tm-article-snippet__title-link").attrs['href']
    hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
    hubs = {hub.find('span').text for hub in hubs}
    data_str = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['datetime']
    data = datetime.strptime(data_str, '%Y-%m-%dT%H:%M:%S.%fZ').date()
    if like_hubs & hubs:
        print(f'Дата публикации: {data},\nНазвание статьи - "{title}", ссылка - {href}')




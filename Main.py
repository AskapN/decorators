import requests
import bs4
from fake_headers import Headers
from Logger_with_params import logger


@logger('log_4.log')
def find_article_in_habr(keywords):
    headers = Headers(browser='chrome', os='win').generate()
    response = requests.get('https://habr.com/ru/feed/', headers=headers)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    articles_list = soup.select('article')
    for article in articles_list:
        post = article.get_text().lower()
        if any(keyword.lower() in post for keyword in keywords):
            date = article.select_one('time')['title']
            title = article.find('h2').get_text().strip()
            link = 'https://habr.com' + article.find('h2').find('a')['href']
            result = f'{date[:9]} – {title} – {link}'
            print(result)


if __name__ == '__main__':
    find_article_in_habr(['дизайн', 'фото', 'web', 'python'])
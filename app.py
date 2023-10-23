import requests
from flask import Flask
import json


# Функция для получения токена
def get_api_token():
    import dotenv

    search_file = dotenv.find_dotenv()
    token = dotenv.get_key(search_file, 'API_TOKEN')

    if not token:
        raise Exception('There are no api token. Write it to .env file')
    return token


api_token = get_api_token()


# Функция для записи постов в json файл
def _save_articles(articles):
    with open('articles.json', 'w') as file:
        json.dump(articles, file)


# Функция для сохранения обложек в папку 'images'
def _save_arts(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    with open(f'images/{filename}', 'wb') as file:
        file.write(r.content)


# Класс для обработки ошибок
class DevToException(Exception):
    pass


# Класс для осуществления работы над постами
class DevArticles:

    def _get_articles_info(self):

        api_token = get_api_token()
        url = 'https://dev.to/api/articles/me'
        headers = {'api-key': api_token}

        response = requests.get(url, headers=headers)
        if not response.ok:
            raise DevToException('Failed to make response for getting articles. ' + str(response.status_code))

        return response.json()

    def download_articles_info(self):
        articles_list = self._get_articles_info()
        _save_articles(articles_list)

    def download_articles_images(self):
        articles_list = self._get_articles_info()
        images_urls = tuple(article_info['cover_image'] for article_info in articles_list)
        for img_url in images_urls:
            _save_arts(img_url)


dev_to = DevArticles()

app = Flask(__name__)


@app.route('/')
def _welcome():
    return "<h1>Welcome</h1>"


@app.route('/user/<name>')
def _user(name):
    return "<h1>Это профиль пользователя %s</h1>" % name


@app.route('/articles')
def _all_articles():
    dev_to.download_articles_info()
    return "Articles were successfully saved to the json file"


@app.route('/covers_images')
def _covers_images():
    dev_to.download_articles_images()
    return "Covers were successfully saved to the 'images'"


if __name__ == '__main__':
    app.run(debug=True)

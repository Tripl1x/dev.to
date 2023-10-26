from .dev_abc import DevRoot
from exceptions import DevException


# Класс для осуществления работы над постами
class DevArticles(DevRoot):

    def __init__(self):
        super().__init__()
        self._sub_url = 'articles'

    def _get_articles_info(self, sub_url=''):
        response = self._make_request('GET', sub_url)
        if not response.ok:
            raise DevException('Ошибка при запросе статей. ' + str(response.status_code))

        return response.json()

    def get_my_articles(self) -> list[dict]:
        articles_list = self._get_articles_info('me')
        return articles_list

    def get_my_articles_images(self) -> tuple:
        articles_list = self._get_articles_info('me')
        images_urls = tuple(article_info['cover_image'] for article_info in articles_list)
        return images_urls

    def get_article_by_url(self, username:str, slug: str, html=False, markdown=False):
        sub_url = f'{username}/{slug}'
        response = self._make_request('GET', sub_url)
        if not response.ok:
            raise DevException('Ошибка при запросе информации о статье. ' + str(response.status_code))

        response = response.json()
        if not html:
            del response['body_html']
        if not markdown:
            del response['body_markdown']
        return response


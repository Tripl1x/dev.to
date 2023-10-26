from .dev_abc import DevRoot
from exceptions import DevException

class DevComments(DevRoot):
    def __init__(self):
        super().__init__()
        self._sub_url = 'comments'

    def get_comments_by_id(self, comment_id: int, html=False):
        response = self._make_request('GET', str(comment_id))
        if not response.ok:
            raise DevException('Ошибка при запросе комментариев. ' + str(response.status_code))

        response = response.json()
        if not html:
            del response['body_html']
        return response

    def get_comments_from_article(self, entity_id, podcast=False):

        params = {'a_id': entity_id} if not podcast else {'p_id': entity_id}
        response = self._make_request('GET', params=params)
        if not response.ok:
            raise DevException('Ошибка при запросе комментариев статьи. ' + str(response.status_code))

        return response.json()

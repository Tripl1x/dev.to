from abc import ABC
from functions import get_api_token
import requests

class DevRoot(ABC):
    def __init__(self):
        API_TOKEN = get_api_token()
        self._sub_url = ''
        self._base_url = 'https://dev.to/api'
        self._headers = {'api-key': API_TOKEN}

    def _prepare_request_method(self, method: str):
        method = str(method).upper()
        methods_list = ('GET', 'POST', 'PUT', 'DELETE', 'PATCH')
        if method not in methods_list:
            raise AppEception(f'Переданный некорректный метод запроса: {method}. Корректные методы: {methods_list}')
        return method

    def _make_request(self, method, sub_url='', headers=None, params=None, json_data=None, form_data=None):
        method = self._prepare_request_method(method)
        sub_url = f'/{sub_url}' if sub_url else ''
        url = f'{self._base_url}/{self._sub_url}' + sub_url
        headers = {**self._headers, **headers} if headers else self._headers
        return requests.request(method, url, headers=headers, params=params, data=form_data, json=json_data)


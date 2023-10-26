from .dev_abc import DevRoot
from exceptions import DevException


class DevUser(DevRoot):
	def __init__(self):
		super().__init__()
		self._sub_url = 'users'

	def get_user_by_id(self, user_id: int):
		response = self._make_request('GET', str(user_id))
		if not response.ok:
		    raise DevException('Ошибка при запросе информации о пользователе. ' + str(response.status_code))

		return response.json()

	def get_myself(self):
		response = self._make_request('GET', 'me')
		if not response.ok:
		    raise DevException('Ошибка при запросе информации о своем аккаунте. ' + str(response.status_code))

		return response.json()
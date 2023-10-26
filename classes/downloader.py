import requests
import json
from exceptions import DevException


class Downloader:
	path = 'download'
	image_path = path + '/images'


	@classmethod
	def save_articles(cls, articles: list[dict]) -> None:
		""""Функция для записи постов в json файл"""
		del articles['body_html']
		del articles['body_markdown']

		with open(f'{path}/articles.json', 'w') as file:
			json.dump(articles, file, indent=4)


	@classmethod
	def save_images(cls, links) -> None:
		"""Функция для сохранения обложек в папку 'images'"""
		if isinstance(links, str):
			links = [links]

		for link in links:
			filename = link.split('/')[-1]
			r = requests.get(link, allow_redirects=True)
			if not r.ok:
			    raise DevException('Ошибка при запросе изображения. ' + str(r.status_code))
			with open(f'{image_path}/{filename}', 'wb') as file:
			    file.write(r.content)

	@classmethod
	def save_user(cls, user):
		""""Функция для сохранения пользователя в json файл"""
		with open(f'{path}/user.json', 'w') as file:
			json.dump(user, file, indent=4)

	@classmethod
	def save_comments(cls, comments):
		""""Функция для сохранения комментариев в json файл"""
		del comments['body_html']

		with open(f'{path}/articles.json', 'w') as file:
			json.dump(comments, file, indent=4)

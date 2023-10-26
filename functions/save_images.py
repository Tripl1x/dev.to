import requests
from exceptions import DevException


# Функция для сохранения обложек в папку 'images'
def save_images(links) -> None:
    if isinstance(links, str):
        links = [links]

    for link in links:
        filename = link.split('/')[-1]
        r = requests.get(link, allow_redirects=True)
        if not r.ok:
            raise DevException('Ошибка при запросе изображения. ' + str(r.status_code))
        with open(f'download/images/{filename}', 'wb') as file:
            file.write(r.content)

from exceptions import AppEception

# Функция для получения токена
def get_api_token() -> str:
    import dotenv

    search_file = dotenv.find_dotenv()
    token = dotenv.get_key(search_file, 'API_TOKEN')

    if not token:
        raise AppEception('Отсутствует api token сайта. Добавьте его в файл .env')
    return token

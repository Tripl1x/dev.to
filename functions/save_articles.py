import json

# Функция для записи постов в json файл
def save_articles(articles: list[dict]) -> None:
    with open('download/articles.json', 'w') as file:
        json.dump(articles, file, indent=4)

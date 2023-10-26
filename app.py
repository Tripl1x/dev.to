import requests
from flask import Flask, request, send_file
import json

from functions import get_api_token, save_images, save_articles
from icecream import ic
from classes import DevArticles, DevComments, DevUser, Downloader
from icecream import ic


app = Flask(__name__)

#  для тестов
# art_id = 99986
# user_id = 101616
# com_id = 'd1a1'
# author = javinpaul
# slug = 10-data-science-and-machine-learning-courses-for-programmers-looking-to-switch-career-57kd
# url = author / slug

@app.get('/')
def _welcome():
    return "<h1>Welcome</h1>"

@app.get('/author')
def _author():
    dev = DevUser()
    author = dev.get_myself()
    return author

@app.get('/author/articles')
def _author_articles():

    dev = DevArticles()
    articles = dev.get_my_articles()

    download = request.args.get('download', False)
    if download:
        Downloader.save_articles(articles)

    return articles

@app.get('/author/image')
def _author_images():

    dev = DevArticles()
    images = dev.get_my_articles_images()

    download = request.args.get('download', False)
    if download:
        Downloader.save_images(images)

    return images


@app.get('/user/<user_id>')
def _user_info(user_id):
    dev = DevUser()
    user = dev.get_user_by_id(user_id)

    download = request.args.get('download', False)
    if download:
        Downloader.save_user(user)
    return user


@app.get('/article/<path:url>')
def _article_info(url):
    html = request.args.get('html', False)

    dev = DevArticles()
    article = dev.get_article_by_url(*url.split('/'), html)

    if html:
        article = article['body_html']

    return article

@app.get('/comment/<comment_id>')
def _get_comment(comment_id):
    html = request.args.get('html', False)

    dev = DevComments()
    comment = dev.get_comments_by_id(comment_id, html)

    download = request.args.get('download', False)
    if download:
        Downloader.save_user(user)

    if html:
        comment = comment['body_html']

    return comment

@app.get('/thread/<article_id>')
def _get_thread(article_id):
    is_podcast = request.args.get('podcast', False)

    dev = DevComments()
    thread = dev.get_comments_from_article(article_id, is_podcast)

    download = request.args.get('download', False)
    if download:
        Downloader.save_user(user)

    return thread


@app.get('/image-example')
def fl():
    return send_file('static/images/background.png', mimetype='image/gif')




if __name__ == '__main__':
    app.run(debug=True)




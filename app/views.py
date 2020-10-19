from flask import render_template
from app import app
from app.request import get_news


@app.route('/')
def index():
    news_results = get_news('popular')
    print(news_results)
    return render_template('index.html', popular=news_results, top_headlines=news_results)

from app import app
import urllib.request, json
from .models import news

News = news.News

# Getting api Keys

api_key = app.config['NEWS_API_KEY']

# Getting the news base url

base_url = app.config['NEWS_API_BASE_URL']


def get_news(everything):
    # Here we define a Movie class
    # and then we create an __init__ method
    # and we pass in the six parameters we want inside our movie objects.
    get_news_url = base_url.format(everything, api_key)

    with urllib.request.urlopen(everything, api_key) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results_list = process_results(news_results_list)

    return news_results


def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        source = news_item.get('source')

        author = news_item.get('author')

        title = news_item.get('title')

        description = news_item.get('description')

        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

    return news_results

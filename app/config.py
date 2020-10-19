class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=apple&from=2020-10-18&to=2020-10-18&{}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass


DEBUG = True

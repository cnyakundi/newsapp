import unittest

from app.models import news

News = news.News


class NewsTest(unittest.TestCase):
    def setUp(self):
        self.news_article = News("Endagnet",
                                 "Andrew Tarantola",
                                 "After Math: Apple's unveils its inaugural 5G phone amid a week of firsts",
                                 "The news cycle has been especially hectic as of late, filled with major "
                                 "revelations, announcements and product premieres seemingly happening right on top "
                                 "of one another. From Apple unveiling the iPhone 12 to Sony revealing the PS5’s user "
                                 "interface — and the P…",
                                 "https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality"
                                 "=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-10"
                                 "%2F9bb85400-0f24-11eb-9ff6-15f915240ed1&client=amp-blogside-v2&signature"
                                 "=02fcea5ae3e514da343523b7d7523f6d8f48a028",
                                 "2020-10-18T15:30:15Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_article, News))

    def test_init(self, source, author, title, description, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95' \
                          '&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2020-10%2F9bb85400' \
                          '-0f24-11eb-9ff6-15f915240ed1&client=amp-blogside-v2&signature' \
                          '=02fcea5ae3e514da343523b7d7523f6d8f48a028'+ urlToImage
        self.publishedAt = publishedAt


if __name__ == ' __main__':
    unittest.main()

class News:

    # Here we define a news  class and
    # then we create an __init__ method
    # and we pass in the  parameters we want inside
    # our news objects.
    def __init__(self, source, author, title, description, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.utlToImage = urlToImage
        self.publishedAt = publishedAt

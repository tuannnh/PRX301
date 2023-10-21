class Movie:
    def __init__(self, movie_id, title, year, description, image_url):
        self.rotten_rating = None
        self.imdb_rating = None
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.description = description
        self.rating = None
        self.ranking = None
        self.review = None
        self.image_url = image_url

    def __str__(self):
        return f"Movie: {self.title} ({self.year})"


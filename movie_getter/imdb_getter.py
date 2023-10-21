import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()


def get_movie_rating(movie_title: str):
    movies = ia.search_movie(movie_title)
    movie = movies[0]
    # Fetch the movie details
    ia.update(movie)
    return movie["rating"]

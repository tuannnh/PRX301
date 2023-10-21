import os
import xml.etree.ElementTree as ET

from typing import List

from models.movie import Movie

MOVIES_XML_PATH = 'data/movies.xml'


def initialize_movies_if_not_exists():
    if os.path.exists(MOVIES_XML_PATH):
        print("File exists! Skip action")
    else:
        print("File does not exist. Create a new one")
        # Create a new XML file
        root = ET.Element("movies")
        tree = ET.ElementTree(root)
        tree.write(MOVIES_XML_PATH)


def get_all_movies():
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    movies = []

    for movie in root.findall('movie'):
        movie_id = movie.find('movie_id').text
        title = movie.find('title').text
        year = movie.find('year').text
        description = movie.find('description').text
        rating = movie.find('rating').text
        imdb_rating = movie.find('imdb_rating').text
        rotten_rating = movie.find('rotten_rating').text
        ranking = movie.find('ranking').text
        review = movie.find('review').text
        image_url = movie.find('image_url').text
        movie_item = Movie(movie_id=movie_id, title=title, year=year, description=description, image_url=image_url)
        movie_item.rating=rating
        movie_item.imdb_rating=imdb_rating
        movie_item.rotten_rating=rotten_rating
        movie_item.ranking=ranking
        movie_item.review=review
        movies.append(movie_item)
    return movies


def sort_movies_by_rating(movies: list) -> List[Movie]:
    sorted_movies = sorted(movies, key=lambda movie: movie.rating)
    return sorted_movies


def record_exists(input_id: str):
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    # set the default return value to false
    return_value = False

    # go through each record to find the one with the specified Email address
    for movie in root.findall('movie'):
        movie_id = movie.find('movie_id').text

        # is the requested id the same as this records id?
        if movie_id == input_id:
            # we have found a match set the return value to true
            return_value = True
    # finally return if the record was found to the caller
    return return_value


def generate_id():
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    max_id = 0
    for contact in root.findall('movie'):
        movie_id = int(contact.find('movie_id').text)
        if movie_id > max_id:
            max_id = movie_id
    return max_id + 1


def create_movie(movie: Movie):
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    # Check if record already existed
    movie_id = movie.movie_id
    exists = record_exists(movie_id)
    if not exists:
        # gt a new id
        generated_id = generate_id()

        # get the field values from the user
        title = movie.title
        year = movie.year
        description = movie.description
        rating = movie.rating
        imdb_rating = movie.imdb_rating
        rotten_rating = movie.rotten_rating
        ranking = movie.ranking
        review = movie.review
        image_url = movie.image_url

        # create a contact element at root level
        new_record = ET.SubElement(root, "movie", id=str(generated_id))

        # add the fields into out new record
        ET.SubElement(new_record, "movie_id", name="movie_id").text = str(generated_id)
        ET.SubElement(new_record, "title", name="title").text = title
        ET.SubElement(new_record, "year", name="year").text = year
        ET.SubElement(new_record, "description", name="description").text = description
        ET.SubElement(new_record, "rating", name="rating").text = rating
        ET.SubElement(new_record, "imdb_rating", name="imdb_rating").text = imdb_rating
        ET.SubElement(new_record, "rotten_rating", name="rotten_rating").text = rotten_rating
        ET.SubElement(new_record, "ranking", name="ranking").text = ranking
        ET.SubElement(new_record, "review", name="review").text = review
        ET.SubElement(new_record, "image_url", name="image_url").text = image_url

        # finally save the update
        tree.write(MOVIES_XML_PATH)
        return [generated_id, title]

    else:
        print("Record already exists! Update the record instead!")


def existing_title(check_title: str):
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    for movie in root.findall('movie'):
        title = movie.find('title').text
        if title == check_title:
            movie_id = movie.find('movie_id').text
            title = movie.find('title').text
            year = movie.find('year').text
            description = movie.find('description').text
            rating = movie.find('rating').text
            imdb_rating = movie.find('imdb_rating').text
            rotten_rating = movie.find('rotten_rating').text
            ranking = movie.find('ranking').text
            review = movie.find('review').text
            image_url = movie.find('image_url').text
            existed_movie = Movie(movie_id=movie_id, title=title, year=year, description=description, image_url=image_url)
            existed_movie.rating=rating
            existed_movie.imdb_rating=imdb_rating
            existed_movie.rotten_rating=rotten_rating
            existed_movie.ranking=ranking
            existed_movie.review=review
            return existed_movie
    return None


def search_movie_by_id(search_movie_id: str):
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    for movie in root.findall('movie'):
        movie_id = movie.find('movie_id').text
        if movie_id == search_movie_id:
            movie_id = movie.find('movie_id').text
            title = movie.find('title').text
            year = movie.find('year').text
            description = movie.find('description').text
            rating = movie.find('rating').text
            imdb_rating = movie.find('imdb_rating').text
            rotten_rating = movie.find('rotten_rating').text
            ranking = movie.find('ranking').text
            review = movie.find('review').text
            image_url = movie.find('image_url').text
            search_result_movie = Movie(movie_id=movie_id, title=title, year=year, description=description, image_url=image_url)
            search_result_movie.rating = rating
            search_result_movie.imdb_rating = imdb_rating
            search_result_movie.rotten_rating = rotten_rating
            search_result_movie.ranking = ranking
            search_result_movie.review = review
            return search_result_movie
    return None


def update_movie(to_update_movie: Movie):
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    for movie in root.findall('movie'):
        movie_id = movie.find('movie_id').text

        if movie_id == to_update_movie.movie_id:
            movie.find('title').text = to_update_movie.title
            movie.find('year').text = to_update_movie.year
            movie.find('description').text = to_update_movie.description
            movie.find('rating').text = str(to_update_movie.rating)
            movie.find('imdb_rating').text = str(to_update_movie.imdb_rating)
            movie.find('rotten_rating').text = str(to_update_movie.rotten_rating)
            movie.find('ranking').text = str(to_update_movie.ranking)
            movie.find('review').text = to_update_movie.review
            movie.find('image_url').text = to_update_movie.image_url

            # save the update
            tree.write(MOVIES_XML_PATH)


def delete_movie(delete_movie_id: str) -> bool:
    tree = ET.parse(MOVIES_XML_PATH)
    root = tree.getroot()
    for movie in root.findall('movie'):

        movie_id = movie.find('movie_id').text
        if movie_id == delete_movie_id:
            root.remove(movie)
            tree.write(MOVIES_XML_PATH)
        else:
            print("Move ID not found! Please refresh!")

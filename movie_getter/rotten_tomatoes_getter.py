import requests,re
from bs4 import BeautifulSoup


# Function to get movie ratings from Rotten Tomatoes
def get_movie_ratings(movie_title):
    # Format the movie title for the URL
    formatted_title = re.sub(r'[^a-zA-Z0-9\s]', '', movie_title).replace(" ", "_").lower()

    # Make a GET request to the Rotten Tomatoes search page
    url = f"https://www.rottentomatoes.com/m/{formatted_title}"
    response = requests.get(url)

    # Check if the movie page exists
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the rating element
        rating_percentage = soup.find('score-icon-critic-deprecated')['percentage']

        if rating_percentage:
            return rating_percentage
        else:
            return -1
    else:
        return -1




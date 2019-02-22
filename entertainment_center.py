import fresh_tomatoes
import media

# Instance of the movie "Life Is beautiful"
life_is_beautiful = media.Movie("Life is Beautiful",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg",  # noqa
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w",)

# Instance of the movie "Leon: The Professional"
the_professional = media.Movie("Leon: The Professional",
                               "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=DcsirofJrlM")

# Instance of the movie "Fight Club"
fight_club = media.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# Set the instances that the website will show
movies = [life_is_beautiful, the_professional, fight_club]
fresh_tomatoes.open_movies_page(movies)  # Open the website

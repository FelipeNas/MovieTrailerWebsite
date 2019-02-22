import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Attributes:
        title: a string with the movie title
        poster_image_url: a string with the link of the movie poster
        trailer_youtube_url: a string with the link of the
        movie youtube trailer
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Movie constructor
        Parameters:
            movie_title: a string with the movie title
            poster_image: a string with the link of the movie poster
            trailer_youtube: a string with the link of the
            movie youtube trailer
        """

        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie():
    """
    This class creates a template for Movie objects,
    which contain a movie's name, storyline summary,
    poster image URL and youtube trailer URL.
    """
    def __init__(self, title, story, poster, trailer):
        """
        Method to initialize a movie object, takes as
        arguments the title, storyline, poster image URL
        and youtube trailer URL for the movie.

        :param title: string
        :param story: string
        :param poster: string
        :param trailer: string
        """
        self.title = title
        self.story = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

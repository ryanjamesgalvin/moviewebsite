class Movie():
    """
    This class creates a template for Movie objects,
    which contain a movie's name, storyline summary,
    poster image URL and youtube trailer URL.
    """
    def __init__(self, title, story, poster, trailer):
        """
        Method to initialize a movie object

        :param title: string, movie title
        :param story: string, movie storyline
        :param poster: string, poster URL
        :param trailer: string, trailer URL
        """
        self.title = title
        self.story = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

import webbrowser

class Movie():
    """Class for movie objects and methods """

    def __init__(self, movie_name, storyline, movie_icon, movie_trl):
        """This method initalizes a movie object with title, story line ,icon and youtube trailer """
        self.title = movie_name
        self.storyline = storyline
        self.poster_image_url = movie_icon
        self.trailer_youtube_url = movie_trl

    def show_trailer(self):
        """ opens up youtube trailer on the movie object"""
        webbrowser.open(self.trailer_youtube_url)

import webbrowser

class Movie():
    def __init__(self, movie_name, movie_icon, movie_trl):
        self.title = movie_name
        #self.story_line = story_line
        self.poster_image_url = movie_icon
        self.trailer_youtube_url = movie_trl

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
import webbrowser

class Movie():
    __doc__ = 'This class provides a way to store movie information'

    def __init__(self, movie_title,movie_storyline, poster_image, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = poster_image
        self.trailer = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)

import webbrowser

class Movie():
    """this class stores information related to the movie
    Attributes:
    title: The title of the video.
    storyline: The storyline about the movie.
    poster_image_url: The poster of the movie.
    trailer_youtube_url: The trailer of the movie"""
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# opens movie trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

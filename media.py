import webbrowser

class Movie():
    """This class is a part of the model, where the
    information of each movie / tv show will be stored.
    It includes the movie title, the storyline, the poster image url
    and also holds the trailer link (youtube).
    Also, a function show_trailer() for launching video.
    """

    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function uses the webbrowser and when called
        it launched the browser and loads the
        url, thus loading the trailer video
        of the calling object.
        """
        webbrowser.open(self.trailer_youtube_url)

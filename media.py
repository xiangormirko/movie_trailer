import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title= title
        self.duration= duration


class Movie(Video):

    """ This is class provides a way to store movie related information"""

    VALID_RATINGS= ["G","PG","PG-13","R"]

    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline= movie_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube

        


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
        
class TvShow(Video):
    def __init__(self, title, duration, show_storyline, poster_image, trailer_youtube, season, episode):
        Video.__init__(self, title, duration)
        self.storyline= show_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube
        self.season= season
        self.episode= episode


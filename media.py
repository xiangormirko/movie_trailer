#!/usr/bin/python
# filename: media.py
# description: Part of the movie trailer website project. This script contains class descriptions for 'Video', 'Movie', and 'TvShow
# author: Xiang Zhao

#need the webbrowser library to open URLs
import webbrowser

#Class Video is parent for both Movie and TvShow. Contains attributes title and duration
class Video():
    def __init__(self, title, duration):
        self.title= title
        self.duration= duration


#Class Movie inherits from class Video. Contains attributes title, duration, movie_storyline, poster_image, trailer_youtube. Has method show_trailer() to open the youtube trailer. 
class Movie(Video):
    #this line will be shown when .__doc__ is called
    """ This is class provides a way to store movie related information"""
    
    #this is an exampler of class variable
    VALID_RATINGS= ["G","PG","PG-13","R"]

    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline= movie_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube

        

    #this is a class method which will open a URL of the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
#Class TvShow inherits form class Video. Contains attributes title, duration, show_storyline, poster_image, trailer_youtube, season, episode        
class TvShow(Video):
    def __init__(self, title, duration, show_storyline, poster_image, trailer_youtube, season, episode):
        Video.__init__(self, title, duration)
        self.storyline= show_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url= trailer_youtube
        self.season= season
        self.episode= episode
        
    #this is a class method which will open a URL of the trailer    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


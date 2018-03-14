import webbrowser

##Google Python Style Guide
##New word:class/instance/constructor/self/instance variable
        ##/instance method/class variable

class Movie():
    ##documentation of Movie class, can alled by __doc__
    """This class provides a way to store movie related information"""
    
    #class variable, can shared by all the instances(all capital letter)
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    ##__means reserved by python
    ##init: create space or memory to remember title, storyline...
    ##self: self or instance been created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title,
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube 
    ##if remove the self, variable cannot be recognized, and can not be called from other files 


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

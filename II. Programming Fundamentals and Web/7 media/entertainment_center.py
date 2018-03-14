import media
import fresh_tomatoes

##self: toy_story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/results?search_query=avatar+trailer")

movies= [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)   ##make a movie website with fresh_tomatoes.py

#print(media.Movie.VALID_RATINGS)  ##print out the class variable

## __dict__  the class name space
## __name__  the name of the class
## __bases__ the classes from which this class inherits
## __doc__   the class documentation string
## __module__ the name of the module in which this class was defined
print(media.Movie.__doc__)    
print(media.Movie.__name__)   
print(media.Movie.__module__) 

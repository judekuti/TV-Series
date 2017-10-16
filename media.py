import webbrowser

class Movie():

# The class Movie holds the constructors using the init method
# The constructors are invoked to create objects from the class blueprint

    def __init__(self,movie_title,valid_rating, movie_storyline, category,
                 poster_image,trailer_youtube, season, episode):
        self.title=movie_title
        self.valid_rating=valid_rating
        self.movie_storyline=movie_storyline
        self.category=category
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.season=season
        self.episode=episode
       
# This function displays the trailer from the youtube trailer link
# which is a video object created and displayed with the webbrowser.open function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

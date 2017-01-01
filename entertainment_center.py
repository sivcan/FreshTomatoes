from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story",
                  "A story of a boy and his toys that come to life",
                  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar",
                "A story about an alien on a planet",
               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

godfather = Movie("Godfather",
                 "Godfather. Need I say more?",
                  "https://s-media-cache-ak0.pinimg.com/originals/f6/9e/c6/f69ec6bc013826e2988c4865f5a1537c.jpg",  # noqa
                  "https://www.youtube.com/watch?v=sY1S34973zA")

transformers = Movie("Transformers",
                     "The noble Autobots and devious Decepticons!",
                     "http://www.firstshowing.net/img/optimus-poster-big.jpg",
                     "https://www.youtube.com/watch?v=dxQxgAfNzyE")

dont_breathe = Movie("Don't Breathe",
                     "A blind man and his story.",
                     "https://upload.wikimedia.org/wikipedia/en/4/41/Don't_Breathe_(2016_film).png",  # noqa
                     "https://www.youtube.com/watch?v=76yBTNDB6vU")

shawshank = Movie("Shawshank Redemption",
                  "Watch it. To Believe it. ;)",
                  "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
                  "https://www.youtube.com/watch?v=6hB3S9bIaco")

# Creating a list of movies from the data.
movies = [toy_story, avatar, godfather, transformers, dont_breathe, shawshank]
# Sending the list of movies to the fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)

# The code section below is to print the doc string, the name and the
# module of the Movie class.
"""print(Movie.VALID_RATINGS)
print(Movie.__doc__)
print(Movie.__name__)
print(Movie.__module__) """

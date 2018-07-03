import media 
import fresh_tomatoes

# creates favourite movies

# ET movie: movie title, storyline, poster image and movie trailer
et = media.Movie("ET The Extra Terrestial",
                 "A boy helps an alien",
                 "https://upload.wikimedia.org/wikipedia/en"
                 "/6/66/E_t_the_extra_terrestrial_ver3.jpg",
                 "https://www.youtube.com/watch?v=DSx8Jobx-Gs")

# IT movie: movie title, storyline, poster image and movie trailer
it = media.Movie("IT",
                 "There is something happening in the town",
                 "https://upload.wikimedia.org/wikipedia/en"
                 "/5/5a/It_%282017%29_poster.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")

# Predator movie: movie title, storyline, poster image and movie trailer
predator = media.Movie("Predator",
                       "There's something out there",
                       "https://upload.wikimedia.org/wikipedia/en"
                       "/9/95/Predator_Movie.jpg",
                       "https://www.youtube.com/watch?v=X2hBYGwKh3I")

# Happy Gilmore movie: movie title, storyline, poster image and movie trailer
happy_gilmore = media.Movie("Happy Gilmore",
                            "a hockey player switches to golf to save his grandmother's house",
                            "https://upload.wikimedia.org/wikipedia/en"
                            "/b/be/Happygilmoreposter.jpg",
                            "https://www.youtube.com/watch?v=y1emDAYCfVQ")

# UP movie: movie title, storyline, poster image and movie trailer
up = media.Movie("UP",
                 "A whole adventure awaits for a man who hasn't lost his young side",
                 "https://upload.wikimedia.org/wikipedia/en"
                 "/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

# Toy Story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie("Toy Story",
                        "the toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en"
                        "/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# the list is stored in a movie object
movies = [et, it, predator, 
          happy_gilmore, up, toy_story]

# A webpage is created with the data inside movies list 
fresh_tomatoes.open_movies_page(movies)

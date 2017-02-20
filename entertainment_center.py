import media
import fresh_tomatoes

# Create a list of movies

toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

avatar = media.Movie("Avatar",
                        "https://upload.wikimedia.org/wikipedia/en/5/5c/Avatar_picture.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                        )
moana = media.Movie("Moana",
                     "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI"
                     )

movies=[toy_story, avatar, moana]

fresh_tomatoes.open_movies_page(movies)
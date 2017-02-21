import media
import fresh_tomatoes

# create instances of movie and add them to a list
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that comes to a life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

avatar = media.Movie("Avatar",
                     "Story about a Marine who visits another planet",
                      "https://upload.wikimedia.org/wikipedia/en/5/5c/Avatar_picture.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                        )
moana = media.Movie("Moana",
                    "Story about a brave Hawaiian princess",
                     "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI"
                     )
movies=[toy_story, avatar, moana]

# This function call uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

import media
import fresh_tomatoes

# create an object for the movie Taken
taken = media.Movie("Taken",
                    "A father's daughter is kidnapped and he goes to rescue her",
                    "https://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg",
                    "https://www.youtube.com/watch?v=pbA-tBrHNfI")

#create an object for the movie Avatar
avatar = media.Movie("Avatar",
                     "A marine in an alien world",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#create an object for the movie Requiem For a Dream
requiem = media.Movie("Requiem For a Dream",
                      "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
                      "https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg",
                      "https://www.youtube.com/watch?v=0nU7dC9bIDg")

#create an object for the movie The Big Lebowski
lebowski = media.Movie("The Big Lebowski",
                       "A man is mistaken for someone famous and gets beaten up as a result, he gets offered a risky high paying job as recompense.",
                       "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")

#create an object for the movie Winchester
winchester = media.Movie("Winchester",
                         "A doctor is hired to assess the mental health of the head of the winchester company, and soon discovers the things plagueing her are supernatural",
                         "https://upload.wikimedia.org/wikipedia/en/d/d4/Winchester_%28film%29.png",
                         "https://www.youtube.com/watch?v=0Juc2cL26mg")

#create an object for the movie Good Will Hunting
good_will_hunting = media.Movie("Good Will Hunting",
                                "A genius works as a janitor at MIT, and gets noticed by a professor after he solves a high level problem",
                                "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
                                "https://www.youtube.com/watch?v=QSMvyuEeIyw")
#create array of movies for calling the open_movies_page method
movies = [taken, avatar, requiem, lebowski, winchester, good_will_hunting]

#call open movies page method from fresh_tomatoes to generate the webpage
fresh_tomatoes.open_movies_page(movies)
                                                       
                               

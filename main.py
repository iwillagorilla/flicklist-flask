import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/movie")
def index():
    # choose a movie by invoking our new function
    movie_for_today = get_random_movie()
    movie_for_tomorrow = get_random_movie()

    while movie_for_today is movie_for_tomorrow:
        movie_for_tomorrow = get_random_movie()
        #runs get random movie for both while they don't match

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>{0}</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content = "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li> {1} </li>"
    content += "</ul>"

    return content.format (movie_for_today, movie_for_tomorrow)

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    
    movie_list = ["Cinderella", "Beauty and the Beast", "Ariel", "Get Shorty", "Lone Ranger",]
    
    return movie_list[random.randint(0, len(movie_list) -1)]
app.run()

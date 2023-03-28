# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """Create dictionary containing title, genre, and rating of a movie
    
    Keyword arguments:
    title -- the title of the movie
    genre -- the genre of the movie
    rating -- the rating of the movie
    """
    # Return None if any parameter is falsy
    if not title or not genre or not rating:
        return None
        
    movie = {
        "title": title, 
        "genre": genre,
        "rating": rating
    }

    return movie

def add_to_watched(user_data, movie):
    """Add a movie to watched list.
    
    Keyword arguments:
    user_data -- dictionary containing movies user has watched
    movie -- dictionary containing title, genre, and rating
    """
    # Check movie isn't empty and is a dictionary
    # Try to add movie to watched, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watched"].append(movie)
        except KeyError:
            print("'Watched' key does not exist; could not add movie")
    
    return user_data

def add_to_watchlist(user_data, movie):
    """Add a movie to a watchlist.
    
    Keyword arguments:
    user_data -- dictionary containing movies user wants to watch
    movie -- dictionary containing title, genre, and rating
    """
    # Check movie isn't empty and is a dictionary
    # Try to add movie to watchlist, otherwise give error message
    if movie and isinstance(movie, dict):
        try:
            user_data["watchlist"].append(movie)
        except KeyError:
            print("'Watchlist' key does not exist; could not add movie")
    
    return user_data

def watch_movie(user_data, title):
    """Move movie if in watchlist to watched
    
    Keyword arguments:
    user_data -- dictionary containing movies user has and wants to watch
    title -- the movie title 
    """
    # Check title is a string and not empty, otherwise return user_data
    if not isinstance(title, str) or not title:
        return user_data

    # Check if movie with title in watchlist
    # If it is, append movie to watched and remove from watchlist
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0
    
    avg_rating = 0 
    for movie in user_data["watched"]:
        avg_rating += movie.get("rating")
    
    return avg_rating / len(user_data["watched"])


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


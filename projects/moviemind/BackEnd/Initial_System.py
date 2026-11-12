from secrets import token_urlsafe

from BackEnd.System import MovieMindSystem
from Dataset import MovieMindProDB


DEMO_MOVIES = (
    ("Signal Beyond Dawn", "Science fiction"),
    ("Orbit in Blue", "Science fiction"),
    ("A Map of Saturn", "Science fiction"),
    ("The Clockwork Harbor", "Adventure"),
    ("A Lantern for June", "Drama"),
    ("Seven Quiet Streets", "Drama"),
    ("Rain on Platform Six", "Mystery"),
    ("The Glass Postcard", "Mystery"),
    ("Moonlit Observatory", "Science fiction"),
    ("The Far Shore", "Adventure"),
    ("Friday at the Bakery", "Comedy"),
    ("The Borrowed Violin", "Drama"),
)

# Ratings use index 0 as the same unused placeholder as the recommender.
DEMO_RATINGS = (
    (0, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 8, 9, 9, 8, 0, 0, 2, 0, 9, 8, 0, 0),
    (0, 2, 3, 2, 0, 9, 8, 9, 8, 0, 2, 7, 9),
)


def initial(database_path):
    MovieMindProDB.dbname = database_path
    MovieMindProDB.create_and_initial_database()
    system = MovieMindSystem()

    for movie_id, (title, genre) in enumerate(DEMO_MOVIES, start=1):
        system.add_movie(movie_id, title, genre, "", "", "", "", "", "", "", if_initial=True)

    for user_id, ratings in enumerate(DEMO_RATINGS, start=1):
        system.create_user(f"demo-{user_id}", token_urlsafe(), f"Demo {user_id}", "", [], [], ratings)

    return system

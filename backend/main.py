from fastapi import FastAPI 
from typing import Union
from movies import Movies

mApp = FastAPI()

movies = Movies("./movies.txt")

@mApp.get("/movie/{movie_id}")
def get_movie_by_name(movie_id: str):
    if 0 <= int(movie_id) < len(movies._movies):
        return movies._movies[int(movie_id)]
    else:
        return None
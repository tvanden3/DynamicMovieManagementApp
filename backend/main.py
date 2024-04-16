from fastapi import FastAPI 
from typing import Union
from movies import Movies
from movies import Movie

mApp = FastAPI()

movies = Movies("./movies.txt")

@mApp.get("/movie/{movie_id}")
def get_movie_by_name(movie_id: str):
    for i in range(0,len(movies._movies),1):
        if movies._movies[i]['id'] == int(movie_id):
            return movies._movies[int(i)]

@mApp.put("/movie/{movie_id}")
def update_movie(movie_id: int, new_movie: Movie) -> Union[Movie, None]:
    for i in range(0,len(movies._movies),1):
        if movies._movies[i]['id'] == movie_id:
            movies._movies[i]['name'] = new_movie.name
            movies._movies[i]['cast'] = new_movie.cast
            return{
                  "id" : new_movie.id,
                  "name": new_movie.name,
                  "cast": new_movie.cast
        }

from fastapi import FastAPI 
from typing import Union
from movies import Movies
from movies import Movie
from movies import Movie2

mApp = FastAPI()

movies = Movies("./movies.txt")

@mApp.get("/movie/{movie_id}")
def get_movie_by_name(movie_id: str):
    for i in range(0,len(movies._movies),1):
        if 'id' in movies._movies[i]:
            if movies._movies[i]['id'] == int(movie_id):
                return movies._movies[int(i)]
        else:
            print(i)
            print(movies._movies[i])
            
        #if movies._movies[i]['id'] == int(movie_id):
        #    return movies._movies[int(i)]

@mApp.put("/movie/{movie_id}")
def update_movie(movie_id: int, new_movie: Movie2) -> Union[Movie, None]:
    for i in range(0,len(movies._movies),1):
        if movies._movies[i]['id'] == movie_id:
            movies._movies[i]['name'] = new_movie.name
            movies._movies[i]['cast'] = new_movie.cast
            return movies._movies[i]


@mApp.delete("/movie/{movie_id}")
def delete_movie(movie_id: int, new_movie: Movie2) -> Union[Movie, None]:
    for i in range(0,len(movies._movies),1):
        if movies._movies[i]['id'] == movie_id :
            id = movies._movies[i]['id']
            name = str(movies._movies[i]['name'])
            cast = movies._movies[i]['cast']

            movies._movies.remove(movies._movies[i])
            return  {
            'id'    : id,
            'name' : name,
            'cast': cast
         }


@mApp.post("/movie/{movie_id}")
def post_movie(new_movie: Movie2) -> Union[Movie, None]:
    newId = len(movies._movies)
    movie = {
        'id': newId,
        'name': new_movie.name,
        'cast': new_movie.cast
    }
    movies._movies.append(movie)
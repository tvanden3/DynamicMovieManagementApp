from typing import List 
from pydantic import BaseModel

class Movie(BaseModel):
    id: int
    name: str
    cast: List[str]

class Movie2(BaseModel):
    name: str
    cast: List[str]

class Movies:
    def __init__(self, movies_file):
        self._movies = []
        with open(movies_file, encoding="utf-8") as file:
            counter = 1
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'id': counter,
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    counter = counter + 1
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )

    def search_movies_by_name(self, keyword):
        matched_movies = []
        for movie in self._movies:
            if keyword.lower() in movie['name'].lower():
                matched_movies.append(movie['name'])

        if matched_movies:
            for movie_name in matched_movies:
                print(movie_name)
        else:
            print("No matching movie found.")

    def list_all_movies(self) :
        for movie in self._movies:
            print(movie['name'])


    def search_movies_by_cast(self, keyword):
        matched_movies = []

        for movie in self.movies:
            matchedcast = []
            for actor in movie['cast']:
                if keyword.lower() in actor.lower():
                    matchedcast.append(actor)
            if matchedcast:
                matched_movies.append({
                    'name': movie['name'],
                    'cast': matched_cast
                })

        if matched_movies:
            for movie in matched_movies:
                print(movie['name'])
                print(movie['cast'])
        else:
            print("\nNo movies matched the search keyword")


if __name__ == "__main__":
    movies = Movies('./movies.txt')
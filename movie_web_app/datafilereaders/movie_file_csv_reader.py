import csv
from typing import List
# from domainmodel.movie import Movie
# from domainmodel.actor import Actor
# from domainmodel.genre import Genre
# from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies: List[Movie] = list()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()


    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            #index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                the_movie = Movie(title, release_year)
                self.__dataset_of_movies.append(the_movie)
                genre = row["Genre"]
                genre_list = genre.split(",")
                for i in genre_list:
                    the_genre = Genre(i)
                    #if the_genre not in self.__dataset_of_genres:
                    self.__dataset_of_genres.add(the_genre)
                the_director = row["Director"]
                director_obj = Director(the_director)
                self.__dataset_of_directors.add(director_obj)
                actor_list = row["Actors"]
                for j in actor_list.split(","):
                    actor_obj = Actor(j)
                    #if j.strip() not in self.__dataset_of_actors:
                    self.__dataset_of_actors.add(actor_obj)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies
    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors
    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors
    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

filename = '/Users/vivian/Desktop/235Ass2/movie_web_app/datafiles'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

all_directors_sorted = sorted(movie_file_reader.dataset_of_directors)
print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')














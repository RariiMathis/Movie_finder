# lib/helpers.py
from models.actor import Actor
from models.movie import Movie

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def get_all_actors():
    print (Actor.all())

def get_all_movies():
    print (Movie.all())

def delete_actor(choice):
    Actor.delete(choice)

def delete_movie(choice):
    Movie.delete_movie(choice)

def add_actor(choice):
    print(Actor.add_actor(choice))

def add_movie(choice):
    print(Movie.add_movie(choice))
    
def search_for_movies(choice):
    print(Movie.search_movies(choice))

def search_by_rating(choice):
    print(Movie.all_rating(choice))


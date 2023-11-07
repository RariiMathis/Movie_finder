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
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
    
def search_movies():
    title = input("Enter the Title to search for: ")
    movies = Movie.search(title = title)
    
    if movies:
        for movie in movies:
            print(f"Title: {movie.title}, Made by: {movie.made}, Year: {movie.year}")
        else:
            print("No movies found with title.")
            
            


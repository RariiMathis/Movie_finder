# lib/helpers.py
from models.actor import Actor

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def get_all_actors():
    print (Actor.all())
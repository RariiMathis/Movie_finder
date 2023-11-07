# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    get_all_actors,
    get_all_movies,
    add_actor
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_actors()
        elif choice == "2":
            get_all_movies()
        elif choice == "3":
           addActor() 
        else:
            print("Invalid choice")
def addActor():
    while True:
        menuAddActor()
        choice = input("> ")
        if choice == "0":
            main()
        else:
            add_actor(choice)

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List All Actors")
    print("2 List All Movies")
    print("3 Add Actor")

def menuAddActor():
    print("Please select an option:")
    print("0. Exit the program")
    print('or start printing new actor')


if __name__ == "__main__":
    main()

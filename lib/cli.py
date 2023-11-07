# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    get_all_actors,
    get_all_movies,
    delete_actor,
    delete_movie,
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
        elif choice == ":)":
            get_all_movies()
        elif choice == "3":
            remove_actor()
        elif choice == "4":
            remove_movie()
        elif choice == '5':
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

def remove_actor():
    while True:
        menu()
        get_all_actors()
        choice = input ("> Enter Actor ID to delete here or 0 to go back -->")
        if choice == "0":
            main()
        # if choice == (self.id):
        delete_actor(choice)

def remove_movie():
    while True:
        menu()
        get_all_movies()
        choice = input ("> Enter Movie ID to delete here or 0 to go back -->")
        if choice == "0":
            main()
        delete_movie(choice)        

        

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List All Actors")
    print("2. List All Movies")
    print("3. Delete Actor")
    print("4. Delete Movie")
    print("5. Add Actor")


def menuAddActor():
    print("Please select an option:")
    print("0. Exit the program")
    print('or start printing new actor')


if __name__ == "__main__":
    main()

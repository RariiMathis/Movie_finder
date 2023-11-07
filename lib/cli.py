# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    get_all_actors,
    get_all_movies,
    search_movies
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
        elif choice == "2" :
            search_movies()    
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List All Actors")
    print(":) List All Movies")
    print("2. Search for Movies")
    

    



if __name__ == "__main__":
    main()

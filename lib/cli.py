# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    get_all_actors,
    get_all_movies,
    search_for_movies,
    delete_actor,
    delete_movie,
    add_actor,
    add_movie,
    search_by_rating,
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
        elif choice == "7" :
            find_movies()    
        elif choice == "3":
            remove_actor()
        elif choice == "4":
            remove_movie()
        elif choice == '5':
             addActor()     
        elif choice == '6':
             addMovie()  
        elif choice == "8":
            find_by_rating()        

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
            
def find_movies():
    while True:
        menu()
        choice = input ("Enter movie title for all movie information:")
        if choice == "0":
            main()
        # if choice == (self.id):
        search_for_movies(choice)


def addMovie():
    while True:
        menuAddMovie()
        choice = input("> ")
        if choice == "0":
            main()
        else:
            add_movie(choice)

def remove_actor():
    while True:
        menu()
        get_all_actors()
        choice = input ("> Enter Actor ID to delete here or 0 to go back -->")
        if choice == "0":
            main()
        delete_actor(choice)

def remove_movie():
    while True:
        menu()
        get_all_movies()
        choice = input ("> Enter Movie ID to delete here or 0 to go back -->")
        if choice == "0":
            main()
        delete_movie(choice) 

def find_by_rating():
    while True:
        menu()
        choice = input ("> Enter Movie Rating here or 0 to go back -->")
        if choice == "0":
            main()
        print("searching")
        search_by_rating(choice)



        

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List All Actors")
    print("2. List All Movies")
    print("3. Delete Actor")
    print("4. Delete Movie")
    print("5. Add Actor")
    print("6. Add Movie")
    print("7. Search for Movies by Title")
    print("8. Search by Rating")

def menuAddActor():
    print("Please select an option:")
    print("0. Exit the program")
    print('or start printing new actor:Name,Age,Origin,Num Of Oscars')


def menuAddMovie():
    print("Please select an option:")
    print("0. Exit the program")
    print('or start printing new movie:title,genre,year,made,rating')

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from helpers import  exit_program, create_exercise, delete_exercise, display_exercises, find_exercise_by_name, create_workout_session, delete_workout_session, display_workout_session, find_workout_session_by_date

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_exercise()
        elif choice == "2":
            delete_exercise()
        elif choice == "3":
            display_exercises()
        elif choice == "4":
            find_exercise_by_name()
        elif choice == "5":
            create_workout_session()
        elif choice == "6":
            delete_workout_session()
        elif choice == "7":
            display_workout_session()
        elif choice == "8":
            find_workout_session_by_date()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create an exercise")
    print("2. Delete an exercise")
    print("3. Display all exercises")
    print("4: Find an exercise by name")
    print("5: Create a workout session")
    print("6: Delete a workout session")
    print("7. Display all workout session")
    print("8. Find workout session by date")

if __name__ == "__main__":
    main()

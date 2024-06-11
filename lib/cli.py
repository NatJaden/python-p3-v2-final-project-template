# from models.exercise import Exercise
# from models.workout_session import WorkoutSession

# def exit_program():
#     print("Exiting the program...")
#     exit()

# def create_exercise():
#     name = input("Enter exercise name: ")
#     category = input("Enter exercise category: ")
#     duration = int(input("Enter exercise duration (in minutes): "))
#     calories_burned = int(input("Enter calories burned: "))

#     try:
#         Exercise.create(name, category, duration, calories_burned)
#         print(f"Exercise {name} created successfully.")
#     except Exception as e:
#         print(f"Error creating exercise: {e}")

# def delete_exercise():
#     exercise_id = input("Enter exercise ID to delete: ")
    
#     try:
#         exercise = Exercise.all.get(int(exercise_id))
#         if exercise:
#             exercise.delete()
#             del Exercise.all[int(exercise_id)]
#             print(f"Exercise with ID {exercise_id} deleted successfully.")
#         else:
#             print(f"No exercise found with ID {exercise_id}.")
#     except Exception as e:
#         print(f"Error deleting exercise: {e}")

# def display_exercises():
#     exercises = Exercise.get_all()
#     for exercise in exercises:
#         print(exercise)

# def create_workout_session():
#     date = input("Enter session date (YYYY-MM-DD): ")
#     duration = int(input("Enter session duration (in minutes): "))
#     notes = input("Enter session notes: ")
#     exercise_id = int(input("Enter exercise ID: "))

#     try:
#         WorkoutSession.create(date, duration, notes, exercise_id)
#         print(f"Workout session created successfully.")
#     except Exception as e:
#         print(f"Error creating workout session: {e}")

# def delete_workout_session():
#     session_id = input("Enter session ID to delete: ")

#     try:
#         session = WorkoutSession.all.get(int(session_id))
#         if session:
#             session.delete()
#             del WorkoutSession.all[int(session_id)]
#             print(f"Workout session with ID {session_id} deleted successfully.")
#         else:
#             print(f"No workout session found with ID {session_id}.")
#     except Exception as e:
#         print(f"Error deleting workout session: {e}")

# def display_workout_sessions():
#     sessions = WorkoutSession.get_all()
#     for session in sessions:
#         print(session)

# def menu():
#     print("\nPlease select an option:")
#     print("0. Exit the program")
#     print("1. Create Exercise")
#     print("2. Delete Exercise")
#     print("3. Display All Exercises")
#     print("4. Create Workout Session")
#     print("5. Delete Workout Session")
#     print("6. Display All Workout Sessions")

# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             create_exercise()
#         elif choice == "2":
#             delete_exercise()
#         elif choice == "3":
#             display_exercises()
#         elif choice == "4":
#             create_workout_session()
#         elif choice == "5":
#             delete_workout_session()
#         elif choice == "6":
#             display_workout_sessions()
#         else:
#             print("Invalid choice")

# if __name__ == "__main__":
#     main()

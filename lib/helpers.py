from models.exercise import Exercise
from models.workout_session import WorkoutSession

def exit_program():
    print("Goodbye!")
    exit()

def create_exercise():
    name = input("Enter exercise name: ")
    category = input("Enter exercise category: ")
    duration = int(input("Enter exercise duration (in minutes): "))
    calories_burned = int(input("Enter calories burned: "))
    try:
        exercise = Exercise.create(name, category, duration, calories_burned)
        print(f'{exercise} created successfully')
    except Exception as exc:
        print("Error creating exercise: ", exc)

def delete_exercise():
    exercise_name= input("Enter the exercise's name: ")
    try:
        if exercise := Exercise.find_by_name(exercise_name):
            exercise.delete()
            print(f'exercise {exercise_name} deleted')
        else:
             print(f'exercise {exercise_name} not found')
    except Exception as e:
        print(f"Error deleting exercise: {e}")

def display_exercises():
    exercise = Exercise.get_all()
    for exercise in exercise:
        print(exercise)

def find_exercise_by_name():
    name = input("Enter the exercise name: ")
    exercise = Exercise.find_by_name(name)
    print(exercise) if exercise else print(
        f'Exercise {name} not found')


def create_workout_session():
    date = input("Enter session date (YYYY-MM-DD): ")
    duration = int(input("Enter session duration (in minutes): "))
    notes = input("Enter session notes: ")
    exercise_id = int(input("Enter exercise ID: "))
    try:
        workout_session = WorkoutSession.create(date, duration, notes, exercise_id)
        print(f'{workout_session} created successfully')
    except Exception as exc:
        print("Error creating workout_session: ", exc)

def delete_workout_session():
    workout_session_date= input("Enter the workout session's date: ")
    try:
        if workout_session := WorkoutSession.find_by_date(workout_session_date):
            workout_session.delete()
            print(f'Workout session on {workout_session_date} deleted')
        else:
             print(f'Workout session on {workout_session_date} not found')
    except Exception as e:
        print(f"Error deleting workout session: {e}")

def display_workout_session():
    workout_session = WorkoutSession.get_all()
    for workout_session in workout_session:
        print(workout_session)

def find_workout_session_by_date():
    date = input("Enter the workout session's date: ")
    workout_session = WorkoutSession.find_by_date(date)
    print(workout_session) if workout_session else print(
        f'Workout session on {date} not found')



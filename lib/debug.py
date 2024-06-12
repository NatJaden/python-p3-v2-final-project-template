#!/usr/bin/env python3
from models.exercise import Exercise
from models.workout_session import WorkoutSession

Exercise.drop_table()

Exercise.create_table()

exercise1 = Exercise.create(
    name="Running",
    category="Cardio",
    duration=30,
    calories_burned=300
)

exercise2 = Exercise.create(
    name="Weightlifting",
    category="Strength Training",
    duration=45,
    calories_burned=200
)

exercise3 = Exercise.create(
    name="Pushups",
    category="Strength Training",
    duration=45,
    calories_burned=500
)
print(Exercise.find_by_name("Weightlifting"))
print(Exercise.get_all())

WorkoutSession.drop_table()

WorkoutSession.create_table()

workout_session1 = WorkoutSession.create(
    date="2024-06-11",
    duration=60,
    exercise_id=exercise1.id,
    notes="Morning workout session"
)

workout_session2 = WorkoutSession.create(
    date="2024-06-10",
    duration=45,
    exercise_id=exercise2.id,
    notes="Evening workout session"
)
workout_session3 = WorkoutSession.create(
    date="2024-07-10",
    duration=60,
    exercise_id=exercise3.id,
    notes="Evening workout session"
)

WorkoutSession.find_by_date("2024-06-11")
print(WorkoutSession.get_all())

### Phase 3 Project

### Fitness Tracker Database

Fitness Tracker Database is a Python CLI application for managing exercise and workout session data using an ORM.

## Installation

Use the package manager pip to install the necessary dependencies from the provided Pipfile.

```
pip install pipenv
pipenv install

```

Usage

```
pipenv shell
python3 cli.py
```

Example Usage
Enter

```
python3 cli.py
```

or

```
./cli.py
```

in the terminal

## CLI

This will launch the CLI application. You can interact with the following options:

Exit
Create Exercise
Delete Exercise
Display All Exercises
Find Exercise by name
Create Workout Session
Delete Workout Session
Display All Workout Sessions
Find Workout Session by name

## ORM Requirements

# Data Model

The data model includes two classes: Exercise and WorkoutSession, with a one-to-many relationship between them.

Exercise
Properties: id, name, category, duration and calories burned
Methods: create, delete, get_all, find_by_name
WorkoutSession
Properties: id, date, duration, notes, exercise_id
Methods: create, delete, get_all, find_by_name

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT

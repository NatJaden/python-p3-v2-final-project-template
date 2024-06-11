from __init__ import CONN, CURSOR

class WorkoutSession:

    all = {}

    def __init__(self, date, duration, notes=None, exercise_id=None, id=None):
        self.id = id
        self.date = date
        self.duration = duration
        self.notes = notes
        self.exercise_id = exercise_id

    def __repr__(self):
        return f"<WorkoutSession {self.date} {self.duration} {self.notes} {self.exercise_id}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE workout_sessions (
                id INTEGER PRIMARY KEY,
                date DATE NOT NULL,
                duration INTEGER NOT NULL,
                notes TEXT,
                exercise_id INTEGER NOT NULL,
                FOREIGN KEY (exercise_id) REFERENCES exercises(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS workout_sessions;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO workout_sessions (
                date, duration, notes, exercise_id
            ) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.date,
                self.duration,
                self.notes,
                self.exercise_id,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, date, duration, notes=None, exercise_id=None):
        workout_session = cls(date, duration, notes, exercise_id)
        workout_session.save()
        return workout_session

    @classmethod
    def instance_from_db(cls, row):
        workout_session = cls.all.get(row[0])

        if workout_session:
            workout_session.date = row[1]
            workout_session.duration = row[2]
            workout_session.notes = row[3]
            workout_session.exercise_id = row[4]

        else:
            workout_session = cls(
                row[1],
                row[2],
                row[3],
                row[4]
            )

            workout_session.id = row[0]

            cls.all[workout_session.id] = workout_session

        return workout_session

    @classmethod
    def find_by_date(cls, date):
        sql = """
            SELECT * FROM workout_sessions WHERE date = ?
        """
        row = CURSOR.execute(sql, (date,)).fetchone()

        if row:
            return cls.instance_from_db(row)

        return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM workout_sessions
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
    def update(self):
        sql = """
            UPDATE workout_sessions SET date = ?, duration = ?, notes = ?, exercise_id = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.date,
                self.duration,
                self.notes,
                self.exercise_id,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM workout_sessions
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

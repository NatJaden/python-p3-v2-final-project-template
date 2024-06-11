from __init__ import CONN, CURSOR

class Exercise:

    all = {}

    def __init__(self, name, category, duration=None, calories_burned=0, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.duration = duration
        self.calories_burned = calories_burned

    def __repr__(self):
        return f"<Exercise {self.name} {self.category} {self.duration} {self.calories_burned}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE exercises (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                duration INTEGER NOT NULL,
                calories_burned INTEGER NOT NULL DEFAULT 0
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS exercises;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO exercises (
                name, category, duration, calories_burned
            ) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.category,
                self.duration,
                self.calories_burned,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, category, duration=None, calories_burned=0):
        exercise = cls(name, category, duration, calories_burned)
        exercise.save()
        return exercise

    @classmethod
    def instance_from_db(cls, row):
        exercise = cls.all.get(row[0])

        if exercise:
            exercise.name = row[1]
            exercise.category = row[2]
            exercise.duration = row[3]
            exercise.calories_burned = row[4]

        else:
            exercise = cls(
                row[1],
                row[2],
                row[3],
                row[4]
            )

            exercise.id = row[0]

            cls.all[exercise.id] = exercise

        return exercise 

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM exercises WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)

        return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM exercises
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
    def update(self):
        sql = """
            UPDATE exercises SET name = ?, category = ?, duration = ?, calories_burned = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.category,
                self.duration,
                self.calories_burned,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM exercises
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

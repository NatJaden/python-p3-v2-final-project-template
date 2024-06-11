from __init__ import CONN, CURSOR

class Author:

    all = {}

    def __init__(
        self, first_name, last_name, nationality=None, birthdate=None, id=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.birthdate = birthdate

    def __repr__(self):
        return f"<Author {self.first_name} {self.last_name} {self.nationality} {self.birthdate}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE authors (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                nationality TEXT,
                birthdate DATE
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS authors;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO authors (
                first_name, last_name, nationality, birthdate
            ) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.nationality,
                self.birthdate,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name, nationality=None, birthdate=None):
        author = cls(first_name, last_name, nationality, birthdate)
        author.save()
        return author

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])

        if author:
            author.first_name = row[1]
            author.last_name = row[2]
            author.nationality = row[3]
            author.birthdate = row[4]

        else:
            author = cls(
                row[1],
                row[2],
                row[3],
                row[4]
            )

            author.id = row[0]

            cls.all[author.id] = author

        return author 

    @classmethod
    def find_by_last_name(cls, last_name):
        sql = """
            SELECT * FROM authors WHERE last_name = ?
        """
        row = CURSOR.execute(sql, (last_name,)).fetchone()

        if row:
            return cls.instance_from_db(row)

        return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM authors
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
    def update(self):
        sql = """
            UPDATE authors SET first_name = ?, last_name = ?, nationality = ?, birthdate = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.nationality,
                self.birthdate,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

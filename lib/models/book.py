from __init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(
        self, title, author_id, genre=None, description=None, id=None
    ):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.description = description

    def __repr__(self):
        return f"<Book {self.title} {self.author_id} {self.genre} {self.description}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author_id INTEGER,
                genre TEXT,
                description TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO books (
                title, author_id, genre, description
            ) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.title,
                self.author_id,
                self.genre,
                self.description,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, author_id, genre=None, description=None):
        book = cls(title, author_id, genre, description)
        book.save()
        return book
    

    def instance_from_db(cls,row):
        book = cls.all.get(row[0])

        if book:
            book.title = row[1]
            book.author_id = row[2]
            book.genre = row[3]
            book.description = row[4]

        else:
            book = cls(
                row[1],
                row[2],
                row[3],
                row[4]
            )

            book.id = row[0]

            cls.all[book.id] = book

        return book 
    
    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT * FROM books WHERE title = ?
        """
        row = CURSOR.execute(sql,(title,)).fetchone()

        print(row)
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        print(rows)
   
    def update(self):
        sql = """
            UPDATE books SET title = ?, author_id = ?, genre = ?, description = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.title,
                self.author_id,
                self.genre,
                self.description,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()




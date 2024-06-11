from book import Book
from author import Author

Author.drop_table()

Author.create_table()

author1 = Author.create(
    first_name="F. Scott",
    last_name="Fitzgerald",
    nationality="American",
    birthdate="1896-09-24"
)

author2 = Author.create(
    first_name="Harper",
    last_name="Lee",
    nationality="American",
    birthdate="1926-04-28"
)
print(Author.find_by_last_name("Lee"))
print(Author.get_all())

Book.drop_table()

Book.create_table()

book1 = Book.create(
    title="The Great Gatsby",
    author_id=author1.id,
    genre="Novel",
    description="A novel by F. Scott Fitzgerald, set in the Roaring Twenties.",
)

book2 = Book.create(
    title="To Kill a Mockingbird",
    author_id=author2.id,
    genre="Fiction",
    description="A novel by Harper Lee, set in the American South during the Great Depression.",
)

# Book.find_by_title("The Great Gatsby")
# print(Book.get_all())



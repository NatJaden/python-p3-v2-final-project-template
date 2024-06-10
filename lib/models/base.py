from book import Book

Book.drop_table()

Book.create_table()

book1 = Book.create(
    title="The Great Gatsby",
    author_id=1,
    genre="Novel",
    description="A novel by F. Scott Fitzgerald, set in the Roaring Twenties.",
)

book2 = Book.create(
    title="To Kill a Mockingbird",
    author_id=2,
    genre="Fiction",
    description="A novel by Harper Lee, set in the American South during the Great Depression.",
)



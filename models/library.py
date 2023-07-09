from models.book import BookNotBorrowedError, BookUnavailableError

class Library:
    def __init__(self) -> None:
        self.books = []
        self.borrowers = []
    def __str__(self) -> str:
        books = ", ".join(str(book.title) for book in self.books)
        borrowers = ", ".join(str(borrower.name) for borrower in self.borrowers)
        return f"Library Collection Informations\nThe books: {books}\nThe borrowers: {borrowers}"
    def add_book(self, book):
        # create a book to collection
        self.books.append(book)
        print(f"Book '{book.title}' has been added to Library.")
    def register_borrower(self, borrower):
        # register new borrower
        self.borrowers.append(borrower)
        print(f"Borrower '{borrower.name}' has been added to Library.")
    def lend_books(self, s_book, s_borrower):
        # if book is availbale we can lend it. so borrower can get it.
        try:
            the_book = self.books[s_book]
            borrower = self.borrowers[s_borrower]
            the_book.borrow()
            borrower.borrow_book(the_book)
            print(f"Library has lent '{the_book.title}' book to borrower '{borrower.name}'.")
        except BookUnavailableError as e:
            print(f"BookUnavailableError: {e}")
    def return_books(self, s_book):
        # update books as available for other borrowers.
        try:
            book = self.books[s_book]
            book.return_book()
            # find the borrower who has this book and remove the book from them.
            for borrower in self.borrowers:
                if book in borrower.borrowed_books:
                    borrower.return_book(book)
        except BookNotBorrowedError as e:
            print(f"BookNotBorrowedError: {e}")
    def display_book_status(self):
        for index, book in enumerate(self.books):
            print(f"ID: {index}\n{book}")
            print("*************************")
    def display_borrower_status(self):
        for index, borrower in enumerate(self.borrowers):
            print(f"ID: {index}\n{borrower}")
            print("*************************")

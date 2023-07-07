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
        print(f"Book '{book.title}' has been added to book collection.")
    def register_borrower(self, borrower):
        # register new borrower
        self.borrowers.append(borrower)
        print(f"Borrower '{borrower.name}' has been added to borrowers collection.")
    def lend_books(self, book, borrower):
        # if book is availbale we can lend it. so borrower can get it.
        if book.availability:
            book.borrow()
            borrower.borrow_book(book)
            print(f"Library has lent '{book.title}' book to borrower '{borrower.name}'.")
        else:
            print(f"'{book.title}' is currently not available, so we can't lend it.")
    def return_books(self, book):
        # update books as available for other borrowers.
        book.return_book()
        # we don't need to remove book from borrower's books list. becouse it's not a real time app.

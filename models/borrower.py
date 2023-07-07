class Borrower:
    def __init__(self, name, borrowed_books = [], fine_amount=0) -> None:
        self.name = name
        self.borrowed_books = borrowed_books
        self.fine_amount = fine_amount
    # This method adds book to borrowed_books list
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"Book '{book.title}' has borrowed by {self.name}.")
    # override built-in method to display Borrower object.
    def __str__(self) -> str:
        borrowed_books = ', '.join([str(book.title) for book in self.borrowed_books])
        return f"Name: {self.name}\nBorrowed Books:\n{borrowed_books}\nFine Amount: {self.fine_amount}"
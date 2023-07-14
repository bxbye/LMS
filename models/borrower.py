
class Borrower:
    def __init__(self, name, borrowed_books = None, fine_amount=0) -> None:
        self.name = name
        self.borrowed_books = borrowed_books or []
        self.fine_amount = fine_amount
    # This method adds book to borrowed_books list
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    def return_book(self, book):
        # should remove from borrowed_books list
        self.borrowed_books.remove(book)
    # override built-in method to display Borrower object.
    def __str__(self) -> str:
        borrowed_books = ', '.join([str(book.title) for book in self.borrowed_books])
        return f"Name: {self.name}\nBorrowed Books:{borrowed_books}\nFine Amount: {self.fine_amount}"
    # does_have(isbn)
    def does_have_book(self, isbn):
        for book in self.borrowed_books:
            if isbn == book.ISBN:
                return True
        return False
from models.book import Book
from models.borrower import Borrower
from models.library import Library

# Create some book instances
book1 = Book("Python Programming", "John Smith", "9781234567890")
book2 = Book("Data Science Basics", "Jane Doe", "9780987654321")

print(book1)

borrower1 = Borrower("Kadir")
borrower2 = Borrower("Ahmet")
borrower1.borrow_book(book1)
borrower1.borrow_book(book2)
print(borrower1)


mylibrary = Library()
mylibrary.add_book(book1)
mylibrary.add_book(book2)
mylibrary.register_borrower(borrower1)
mylibrary.register_borrower(borrower2)

print(mylibrary)

# lend books
mylibrary.lend_books(book1, borrower1)
mylibrary.lend_books(book2, borrower1)
mylibrary.return_books(book1)
mylibrary.lend_books(book1, borrower2)
# Define custom exceptions...
class BookUnavailableError(Exception):
    pass
class BookNotBorrowedError(Exception):
    pass
class Book:
    # constructor
    def __init__(self, title, author, ISBN, availability = True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
    # print(object) or str(object.__str__()) functions invokes this method
    def __str__(self) -> str:
        availability = "Available" if self.availability else "Not Available"
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nAvailability: {availability}"
    # equal comparison
    def __eq__(self, __value: object) -> bool:
        if self.title == __value.title and self.author == __value.author:
            return True
        return False
    # methods and behaviours
    def borrow(self):
        if self.availability:
            self.availability = False
        else:
            raise BookUnavailableError(f"The book '{self.title}' is currently not available.")
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"The book {self.title} has been returned.")
        else:
            raise BookNotBorrowedError(f"The book '{self.title}' has already been returned.")
    
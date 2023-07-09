"""
Author: Kadir KAYA
Date: 9 Jul, 2023
"""
from models.book import Book
from models.borrower import Borrower
from models.library import Library
from faker import Faker

fake = Faker()
kadir_library = Library()
def display_menu():
    print("Menu:")
    print("1. Add Book")
    print("2. Register Borrower")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display Book Status")
    print("6. Display Borrower Status")
    print("0. Exit")

def option1():
    print("Executing 1. Add Book...")
    
    #print(f"Title: {fake.catch_phrase()}\nAuthor: {fake.name()}\nISBN: {fake.isbn13()}")
    new_book = Book(fake.catch_phrase(), fake.name(), fake.isbn13())
    kadir_library.add_book(new_book)
def option2():
    print("Executing 2. Register Borrower...")
    #print(f"Borrower Name: {fake.name()}")
    new_borrower = Borrower(fake.name())
    kadir_library.register_borrower(new_borrower)

def option3():
    print("Executing 3. Lend Book...")
    # get selection from user interface
    s_book = int(input("Select book_id to lend: "))
    s_borrower = int(input("Select borrower_id to lend: "))
    print(f"book_id: {s_book}, borrower_id: {s_borrower}")
    # run methods for lending
    kadir_library.lend_books(s_book, s_borrower)

def option4():
    print("Executing 4. Return Book...")
    # display books for select id of will returning book
    s_book = int(input("Select book_id to return: "))
    kadir_library.return_books(s_book)

def option5():
    print("Executing 5. Display Book Status...")
    kadir_library.display_book_status()

def option6():
    print("Executing 6. Display Borrower Status...")
    kadir_library.display_borrower_status()


# Main menu loop
while True:
    display_menu()
    choice = input("Enter your choice (0-6): ")

    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        option4()
    elif choice == '5':
        option5()
    elif choice == '6':
        option6()
    elif choice == '0':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


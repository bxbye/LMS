import tkinter as tk
from models.book import Book
from models.borrower import Borrower
from models.library import Library
from faker import Faker

fake = Faker()
kadir_library = Library()

def add_book():
    print("Executing 1. Add Book...")
    new_book = Book(fake.catch_phrase(), fake.name(), fake.isbn13())
    kadir_library.add_book(new_book)

def register_borrower():
    print("Executing 2. Register Borrower...")
    new_borrower = Borrower(fake.name())
    kadir_library.register_borrower(new_borrower)

def lend_book():
    print("Executing 3. Lend Book...")
    s_book = int(book_id_entry.get())
    s_borrower = int(borrower_id_entry.get())
    kadir_library.lend_books(s_book, s_borrower)
    display_book_status()

def return_book():
    print("Executing 4. Return Book...")
    s_book = int(return_book_id_entry.get())
    kadir_library.return_books(s_book)
    display_book_status()

def display_book_status():
    print("Executing 5. Display Book Status...")
    book_status_text.delete(1.0, tk.END)
    book_status_text.insert(tk.END, "Book Status:\n")
    # Retrieve and display the book status information
    book_status_text.insert(tk.END, kadir_library.get_book_status())

def display_borrower_status():
    print("Executing 6. Display Borrower Status...")
    borrower_status_text.delete(1.0, tk.END)
    borrower_status_text.insert(tk.END, "Borrower Status:\n")
    # Retrieve and display the borrower status information
    borrower_status_text.insert(tk.END, kadir_library.get_borrower_status())

def exit_program():
    print("Exiting the program...")
    window.quit()

# Create a main window
window = tk.Tk()
window.title("Library Management System")
window.geometry("600x800")  # Set the dimensions of the window (width x height)


# Create UI elements (labels, buttons, entry fields, text widgets, etc.)
menu_label = tk.Label(window, text="Menu:")
menu_label.pack()

button1 = tk.Button(window, text="Add Book", command=add_book)
button1.pack()

button2 = tk.Button(window, text="Register Borrower", command=register_borrower)
button2.pack()

button3 = tk.Button(window, text="Lend Book", command=lend_book)
button3.pack()

button4 = tk.Button(window, text="Return Book", command=return_book)
button4.pack()

button5 = tk.Button(window, text="Display Book Status", command=display_book_status)
button5.pack()

button6 = tk.Button(window, text="Display Borrower Status", command=display_borrower_status)
button6.pack()

button0 = tk.Button(window, text="Exit", command=exit_program)
button0.pack()

book_id_label = tk.Label(window, text="Book ID:")
book_id_label.pack()
book_id_entry = tk.Entry(window)
book_id_entry.pack()

borrower_id_label = tk.Label(window, text="Borrower ID:")
borrower_id_label.pack()
borrower_id_entry = tk.Entry(window)
borrower_id_entry.pack()

return_book_id_label = tk.Label(window, text="Book ID to Return:")
return_book_id_label.pack()
return_book_id_entry = tk.Entry(window)
return_book_id_entry.pack()

book_status_label = tk.Label(window, text="Book Status:")
book_status_label.pack()
book_status_text = tk.Text(window, height=10, width=100)
book_status_text.pack()

borrower_status_label = tk.Label(window, text="Borrower Status:")
borrower_status_label.pack()
borrower_status_text = tk.Text(window, height=10, width=100)
borrower_status_text.pack()

# Start the main event loop
window.mainloop()

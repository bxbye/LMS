# Library Management System
Description:
Create a Library Management System that allows users to manage books, borrowers, and library transactions. The system should support functionalities such as adding books to the library, lending books to borrowers, returning books, and displaying the status of books and borrowers.

Releaase Notes (7 Jul, 2023)
Classes implemented.

Release Notes (9 Jul, 2023)
Implement appropriate error handling for scenarios such as borrowing an unavailable book or returning a book that was not borrowed.
Create a menu-driven interface that allows users to interact with the Library Management System. The menu should include options to add books, register borrowers, lend books, return books, display book status, display borrower status, and exit the program.


I accured a logical error about class's constructor's default parameter. I has been assigned an empty array like: [] as default and i initialized it inside of constructor. But I should have been use default constructor as None parameter. Otherwise empty string at default parameter always update itself. It's so global. So Each object of that class was the same list because of the problem. I've fixed it with None value.
I've used OOP principles in this project.
Of course this project could be optimized. Please, don't hesitate to optimize this codes as fork this repository.

I've created a menu-driven user interface in menu.py file. Users can interact with this library management project as running menu.py file.
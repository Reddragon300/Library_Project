# Library Management System

This is a Python program that models a simple library management system. It allows you to manage books and patrons, check out and return books, and perform various library-related operations.

First Part - 
A simple software system for a library models a library as a collection of books and patrons.
A patron can have as many as 3 books out on loan at any given time. 
Each book has a title, an author, a patron to whom it has been checked out, and a list of patrons waiting for that book to be returned.
When a patron wants to borrow a book, that patron is automatically added to the book's wait list if the book is already checked out. 
When a patron returns a book, it is automatically loaned to the firstpatron on it's wait list who can check out a book.
Each patron has a name and the number of books that patron has currently checked out. Develop the classes Book and Patron to model these objects. 
Think first of the interface or set of methods to be used with each class, and then choose appropriate data structures for the state of the objects. 
Also write a short script to test these classes.

PART 2 - 
Develop a Library class that can manage the books and patrons from Part 1. 
This class should include methods for adding, removing, and finding books and patrons.

PART 3 - 
Develop a Manager class that provides a menu-driven command processor for managing a library of the type developed in Part 2.


## How to Use

1. Clone the repository to your local machine using the following command:
```python
git clone https://github.com/Reddragon300/Library_Project.git
```
2. Navigate to the project directory:
```python
cd Library_Project
```
4. Install any required dependencies (if applicable).

5. Run the program:
```python
python main.py
```
7. Follow the on-screen menu to interact with the library management system.

## Testing

The program includes some basic tests to ensure the functionality of the classes. To run the tests, execute the following command in the project directory:
```python
python test.py
```

The tests will validate the behavior of the Book and Patron classes, as well as the Library and Manager classes.

Feel free to modify and extend the program as needed for your specific requirements.


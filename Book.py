'''
First Part - A simple software system for a library models a library as a collection of books and patrons. A patron can have as many as 3 books out on loan at any given time. Each book has a title, an author, a patron to whom it has been checked out, and a list of patrons waiting for that book to be returned. When a patron wants to borrow a book, that patron is automatically added to the book's wait list if the book is already checked out. When a patron returns a book, it is automatically loaned to the firstpatron on it's wait list who can check out a book. Each patron has a name and the number of books that patron has currently checked out. Develop the classes Book and Patron to model these objects. Think first of the interface or set of methods to be used with each class, and then choose appropriate data structures for the state of the objects. Also write a short script to test these classes.
PART 2 - Develop a Library class that can manage the books and patrons from Part 1. This class should include methods for adding, removing, and finding books and patrons.
PART 3 - Develop a Manager class that provides a menu-driven command processor for managing a library of the type developed in Part 2.
'''

# Represents a book in the library.


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out_to = None  # Patron who has checked out the book.
        self.waiting_list = []  # List of patrons waiting for the book.

   # Adds a patron to the waiting list.
    def add_to_waiting_list(self, patron):
        self.waiting_list.append(patron)

   # Removes a patron from the waiting list.
    def remove_from_waiting_list(self, patron):
        self.waiting_list.remove(patron)

   # Checks out a book to a patron.
    def check_out(self, patron):
        if self.checked_out_to == None:
            self.checked_out_to = patron
            patron.add_book(self)
        else:
            self.add_to_waiting_list(patron)

   # Returns a book to the library.
    def return_book(self):
        if self.checked_out_to:
            patron = self.checked_out_to
            self.checked_out_to = None
            patron.remove_book(self)
            if self.waiting_list:
                next_patron = self.waiting_list.pop(0)
                self.check_out(next_patron)

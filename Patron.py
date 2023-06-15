
#  Represents a library patron.

class Patron:

    def __init__(self, name):
        self.name = name
        self.checked_out_books = []  # List of books checked out by the patron.

    def add_book(self, book):
        self.checked_out_books.append(book)

    def remove_book(self, book):
        self.checked_out_books.remove(book)

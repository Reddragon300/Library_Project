
#  Represents the library itself.
class Library:

    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        self.patrons.remove(patron)

     # Finds a book by its title.
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

     # Finds a patron by their name.
    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        return None

import unittest
from Library import Library
from Book import Book
from Patron import Patron


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book = Book("Python Programming", "John Doe")
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        book = Book("Python Programming", "John Doe")
        self.library.add_book(book)
        self.library.remove_book(book)
        self.assertEqual(len(self.library.books), 0)

    def test_add_patron(self):
        patron = Patron("Alice")
        self.library.add_patron(patron)
        self.assertEqual(len(self.library.patrons), 1)

    def test_remove_patron(self):
        patron = Patron("Alice")
        self.library.add_patron(patron)
        self.library.remove_patron(patron)
        self.assertEqual(len(self.library.patrons), 0)

    def test_checkout_book(self):
        book = Book("Python Programming", "John Doe")
        patron = Patron("Alice")
        self.library.add_book(book)
        self.library.add_patron(patron)
        self.library.checkout_book(book.title, patron.name)
        self.assertEqual(book.checked_out_to, patron)
        self.assertEqual(len(patron.checked_out_books), 1)

    def test_return_book(self):
        book = Book("Python Programming", "John Doe")
        patron = Patron("Alice")
        self.library.add_book(book)
        self.library.add_patron(patron)
        self.library.checkout_book(book.title, patron.name)
        self.library.return_book(book.title)
        self.assertIsNone(book.checked_out_to)
        self.assertEqual(len(patron.checked_out_books), 0)


if __name__ == '__main__':
    unittest.main()


from Library import Library
from Book import Book
from Patron import Patron

# Provides a menu-driven command processor for managing the library.


class Manager:
    def __init__(self):
        self.library = Library()

     # Shows list of options available to the user.
    def display_menu(self):
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Patron")
        print("4. Remove Patron")
        print("5. Checkout Book")
        print("6. Return Book")
        print("7. Quit")

     # Processes the user's choice.
    def process_choice(self, choice):
        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.remove_book()
        elif choice == '3':
            self.add_patron()
        elif choice == '4':
            self.remove_patron()
        elif choice == '5':
            self.check_out_book()
        elif choice == '6':
            self.return_book()
        elif choice == '7':
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book = Book(title, author)
        self.library.add_book(book)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        book = self.library.find_book(title)
        if book:
            self.library.remove_book(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def add_patron(self):
        name = input("Enter the name of the patron: ")
        patron = Patron(name)
        self.library.add_patron(patron)
        print("Patron added successfully.")

    def remove_patron(self):
        name = input("Enter the name of the patron to remove: ")
        patron = self.library.find_patron(name)
        if patron:
            self.library.remove_patron(patron)
            print("Patron removed successfully.")
        else:
            print("Patron not found.")

    def check_out_book(self):
        title = input("Enter the title of the book to check out: ")
        book = self.library.find_book(title)
        if book:
            patron_name = input(
                "Enter the name of the patron checking out the book: ")
            patron = self.library.find_patron(patron_name)
            if patron:
                book.check_out(patron)
                print("Book checked out successfully.")
            else:
                print("Patron not found.")
        else:
            print("Book not found.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        book = self.library.find_book(title)
        if book:
            book.return_book()
            print("Book returned successfully.")
        else:
            print("Book not found.")

    def run(self):
        choice = ''
        while choice != '7':
            self.display_menu()
            choice = input("Enter your choice: ")
            self.process_choice(choice)


manager = Manager()
manager.run()

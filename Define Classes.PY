class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def borrow(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def return_book(self):
        self.quantity += 1


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 3 and book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self):
        self.book_catalog = []

    def add_book(self, title, author, quantity):
        self.book_catalog.append(Book(title, author, quantity))

    def search_books(self, title):
        return [book for book in self.book_catalog if title.lower() in book.title.lower()]

    def view_borrowed_books(self, users):
        borrowed = []
        for user in users:
            for book in user.borrowed_books:
                borrowed.append((user.name, book.title))
        return borrowed

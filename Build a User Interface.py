def main():
    library = Library()
    users = [
        User("Alice", "Borrower"),
        User("Bob", "Borrower"),
        User("Librarian", "Librarian"),
    ]

    while True:
        print("\nLibrary Management System")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            user = next((u for u in users if u.name == username), None)

            if user:
                if user.role == "Borrower":
                    borrower_menu(library, user)
                elif user.role == "Librarian":
                    librarian_menu(library, users)
            else:
                print("User not found.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")


def borrower_menu(library, user):
    while True:
        print("\nBorrower Menu")
        print("1. Search Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title to search: ")
            books = library.search_books(title)
            if books:
                for i, book in enumerate(books):
                    print(f"{i + 1}. {book.title} by {book.author} (Available: {book.quantity})")
            else:
                print("No books found.")
        elif choice == "2":
            title = input("Enter book title to borrow: ")
            books = library.search_books(title)
            if books:
                book = books[0]
                if user.borrow_book(book):
                    print(f"Successfully borrowed {book.title}.")
                else:
                    print("Cannot borrow the book. Either limit reached or unavailable.")
            else:
                print("Book not found.")
        elif choice == "3":
            title = input("Enter book title to return: ")
            books = library.search_books(title)
            if books:
                book = books[0]
                if user.return_book(book):
                    print(f"Successfully returned {book.title}.")
                else:
                    print("You have not borrowed this book.")
            else:
                print("Book not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


def librarian_menu(library, users):
    while True:
        print("\nLibrarian Menu")
        print("1. Add Book")
        print("2. View Borrowed Books")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            quantity = int(input("Enter quantity: "))
            library.add_book(title, author, quantity)
            print("Book added successfully.")
        elif choice == "2":
            borrowed = library.view_borrowed_books(users)
            if borrowed:
                for name, title in borrowed:
                    print(f"{name} borrowed {title}")
            else:
                print("No books are currently borrowed.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

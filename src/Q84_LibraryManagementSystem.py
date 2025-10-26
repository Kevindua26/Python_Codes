# Write a program to build a real world OOP case study (Library Management System).
print('Q84_LibraryManagementSystem.py')

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
    
    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully")
    
    def display_books(self):
        print("\n=== Library Books ===")
        for book in self.books:
            book.display()
    
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' issued successfully")
                else:
                    print(f"Book '{book.title}' is already issued")
                return
        print("Book not found")
    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' returned successfully")
                else:
                    print(f"Book '{book.title}' was not issued")
                return
        print("Book not found")

# Create library
library = Library()

# Add books
library.add_book(Book(1, "Python Programming", "John Smith"))
library.add_book(Book(2, "Data Structures", "Jane Doe"))
library.add_book(Book(3, "Web Development", "Bob Wilson"))

# Display all books
library.display_books()

# Issue a book
print()
library.issue_book(1)

# Display books after issuing
library.display_books()

# Return a book
print()
library.return_book(1)

# Display books after return
library.display_books()

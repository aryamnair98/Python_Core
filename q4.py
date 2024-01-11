class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        available_books = [book for book in self.books if book.is_available]
        for book in available_books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def display_members(self):
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}")

    def borrow_book(self, member_id, book_id):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in self.books if book.book_id == book_id and book.is_available), None)
        if member and book:
            member.books_borrowed.append(book)
            book.is_available = False
            print(f"{member.name} has successfully borrowed '{book.title}'.")

    def return_book(self, member_id, book_id):
        member = next((member for member in self.members if member.member_id == member_id), None)
        book = next((book for book in member.books_borrowed if book.book_id == book_id), None)
        if member and book:
            member.books_borrowed.remove(book)
            book.is_available = True
            print(f"{member.name} has successfully returned '{book.title}'.")



library = Library()
book1 = Book(1, "Introduction to Python", "John Smith")
book2 = Book(2, "Data Structures and Algorithms", "Jane Doe")
member1 = Member(101, "Arya")
member2 = Member(102, "Amal")

library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)

print("Available Books:")
library.display_books()
print("Library Members:")
library.display_members()

library.borrow_book(101, 1)
library.borrow_book(102, 2)

print("Available Books after Borrowing:")
library.display_books()
library.return_book(101, 1)
print("Available Books after Returning:")
library.display_books()
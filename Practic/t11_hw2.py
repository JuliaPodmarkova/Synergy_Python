# Задача 2. Библиотечная

class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def __str__(self):
        return f'"{self.title}" автор {self.author}, год издания книги({self.published_year})'

class Library:
    def __init__(self):
        self.books = []

    def add_new_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" добавлена в библиотеку.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книга "{title}" удалена из библиотеки.')
                return
        print(f'Книга "{title}" не найдена в библиотеке.')

    def list_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
            return
        print("Список книг в библиотеке:")
        for book in self.books:
            print(book)

library = Library()

book1 = Book("1984", "Джордж Оруэлл", 1949)
book2 = Book("Война и мир", "Лев Толстой", 1869)
book3 = Book("Убить пересмешника", "Харпер Ли", 1960)

library.add_new_book(book1)
library.add_new_book(book2)
library.add_new_book(book3)

library.list_books()

library.remove_book("1984")
library.list_books()

library.remove_book("Неизвестная книга")

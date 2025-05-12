class Book:
    total_books = 0
    @classmethod
    def increament_book_count(cls, book_name):
        if book_name:
            cls.total_books += 1

book = Book()
book.increament_book_count("Karsaz")
book.increament_book_count("Khilam")
book.increament_book_count("Battle of Badr")
print(book.total_books)
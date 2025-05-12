import json
import os

data_file = "plm.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {}

def save_data(library):
    with open(data_file, 'w') as f:
        json.dump(library, f)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_data(library)
    print(f"Book '{title}' added to the library.")

def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ")
    initial_length = len(library)
    library[:] = [book for book in library if book["title"].lower() != title.lower()]
    if len(library) < initial_length:
        save_data(library)
        print(f"Book '{title}' removed from the library.")
    else:
        print(f"Book '{title}' not found in the library.")

def search_library(library):
    search_by = input("Search by title or author: ").lower()
    while search_by not in ['title', 'author']:
        print("Please enter either 'title' or 'author'")
        search_by = input("Search by title or author: ").lower()
    
    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            status = "Read" if book["read"] else "Not Read"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(f"\nNo books found for {search_by} '{search_term}'.")

def display_all_books(library):
    if not library:
        print("No books in the library.")
        return
    
    print("\nAll Books in Library:")
    for book in library:
        status = "Read" if book["read"] else "Unread"
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    
    read_books = len([book for book in library if book["read"]])
    percentage_read = (read_books / total_books) * 100
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            save_data(library)  # Save before exiting
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
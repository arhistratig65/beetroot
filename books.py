import json
import datetime

# Книги
BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.datetime(2023, 11, 15, 12, 13, 14),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.datetime(2023, 12, 16, 20, 0, 11),
    },
    {
        "name": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.datetime(2021, 10, 30, 7, 43, 28),
    },
]

# Запись в JSON-файл


def save_books_to_json(books, filename):
    # Из entry_added в POSIX timestamp
    for book in books:
        book['entry_added'] = int(book['entry_added'].timestamp())

    # Запись в файл JSON
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)


if __name__ == "__main__":
    # Сохранение книг в JSON-файл
    save_books_to_json(BOOKS, 'books.json')

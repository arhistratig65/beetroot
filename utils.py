import datetime
import random
import logging  # Додав імпорт модуля логування

# Налаштування логування
logging.basicConfig(filename='/book_utils.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Початкові дані про книги
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

# Функція для відображення усіх книг з логуванням
def show_all_books(books):
    logging.info("User is viewing a list of books")  # Запис логу
    print("Books:")
    for book in books:
        print(f"'{book['name']}' by {book['author']} is {book['genre']} and has {book['pages']} pages")
        print("=" * 60)

# Функція для додавання нової книги з логуванням
def add_new_book(books):
    logging.info("User is adding new book")  # Запис логу
    name = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    genre = input("Введіть жанр книги: ")

    while True:
        pages_input = input("Введвть кількість сторінок (опціонально): ")
        if not pages_input:
            pages = None  # Якщо користувач не ввів нічого, то None
            break
        try:
            pages = int(pages_input)  # Спробуємо перевести введене значення у ціле число
            break
        except ValueError:
            print("Введіть коректне значення кількості сторінок.")

    entry_added = datetime.datetime.now()

    books.append({
        "name": name,
        "author": author,
        "genre": genre,
        "pages": pages,
        "entry_added": entry_added,
    })
    print("Книгу додано!")

# Функція для випадкового вибору книги з логуванням
def choose_random_book(books):
    logging.info("User is choosing a random book")  # Запис логу
    if books:
        random_book = random.choice(books)
        print("Випадково обрана книга:")
        print(f"'{random_book['name']}' by {random_book['author']} is {random_book['genre']} and has {random_book['pages']} pages")
    else:
        print("Список книг порожній.")
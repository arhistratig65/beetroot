from post import Post

if __name__ == "__main__":
    while True:
        print("Добро пожаловать в новую социальную сеть")
        message = ("""
            Выберите опцию:
            1. Добавить пост
            2. Просмотреть все посты
            3. Поставить лайк посту
            4. Поставить дизлайк посту
            0. Выйти

            Ваш выбор: """)
        choice = input(message)
        match choice:
            case "1":
                Post()
            case "2":
                Post.show_posts()
            case "3":
                Post.like()
            case "4":
                Post.dislike()
            case "0":
                break
            case _:
                print("Неправильный выбор")

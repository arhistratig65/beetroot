from datetime import datetime, timedelta


class Content:

    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.author} сказал в {self.created_at}: {self.text}"


class Post(Content):

    entries = list()

    def __init__(self):
        super().__init__()
        self.entries.append(self)
        self.id = len(self.entries)
        self.likes = 0
        self.dislikes = 0

    def __str__(self):
        return (f"#{self.id} {self.author} said: {self.text}. "
                f"Likes: {self.likes} | Dislikes: {self.dislikes}")

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.rating == other.rating
        return False

    def __lt__(self, other):
        if isinstance(other, Post):
            return self.rating < other.rating
        return False

    def __le__(self, other):
        if isinstance(other, Post):
            return self.rating <= other.rating
        return False

    def __gt__(self, other):
        if isinstance(other, Post):
            return self.rating > other.rating
        return False

    def __ge__(self, other):
        if isinstance(other, Post):
            return self.rating >= other.rating
        return False

    @staticmethod
    def week_ago():
        return datetime.now() - timedelta(days=7)

    @classmethod
    def show_last_week(cls):
        for entry in cls.entries:
            if entry.created_at > cls.week_ago():
                print(entry)

    @classmethod
    def show_posts(cls):
        for entry in sorted(cls.entries, reverse=True):
            print(entry)

    @classmethod
    def find_by_id(cls, post_id):
        for post in cls.entries:
            if post.id == int(post_id):
                return post
        return None

    @classmethod
    def like(cls):
        post_id = input("Enter post id: ")
        post = cls.find_by_id(post_id)
        if post:
            post.likes += 1
        else:
            print("Post not found!")

    @classmethod
    def dislike(cls):
        post_id = input("Enter post id: ")
        post = cls.find_by_id(post_id)
        if post:
            post.dislikes += 1
        else:
            print("Post not found!")

    @property
    def rating(self):
        return self.likes - self.dislikes


class Comment(Content):

    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} commented on post #{self.post_id}: {self.text}"


if __name__ == "__main__":

    post1 = Post()  # Создается первый пост
    post2 = Post()  # Создается второй пост
    post1.likes += 1  # Лайк к первому посту
    post2.dislikes += 1  # Дизлайк ко второму посту
    print(post1 == post2)  # Сравниваются два поста по их рейтингу

class FibonacciIterator:
    def __init__(self, limit):
        self.a, self.b = 1, 2  # Початкові значення послідовності Фібоначчі
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a >= self.limit:
            raise StopIteration
        current = self.a
        # Перехід до наступних чисел послідовності
        self.a, self.b = self.b, self.a + self.b
        return current


def sum_even_fibonacci(limit):
    sum_even = 0
    for number in FibonacciIterator(limit):
        if number % 2 == 0:
            sum_even += number
    return sum_even


# Встановлення ліміту
limit = 4000000

# Виклик функції та виведення результату
print(sum_even_fibonacci(limit))

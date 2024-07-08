class Calc:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def pow(a, b):
        return a ** b

    @staticmethod
    def div(a, b):
        if b == 0:
            raise ValueError("Неможливо поділити на нуль")
        return a / b

    @staticmethod
    def floordiv(a, b):
        if b == 0:
            raise ValueError("Неможливо поділити на нуль")
        return a // b

    @staticmethod
    def mod(a, b):
        if b == 0:
            raise ValueError("Неможливо поділити на нуль")
        return a % b

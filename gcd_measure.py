import time
import logging
from math import gcd as math_gcd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Декоратор для вимірювання часу виконання функцій


def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Function {func.__name__} execution time: {
                    execution_time} seconds")
        return result, execution_time
    return wrapper

# Функція знаходження GCD через віднімання


@log_decorator
def gcd_subtraction(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

# Функція знаходження GCD через залишок від ділення


@log_decorator
def gcd_modulus(a, b):
    while b:
        a, b = b, a % b
    return a

# Функція знаходження GCD з використанням вбудованої функції з модулю math


@log_decorator
def gcd_builtin(a, b):
    return math_gcd(a, b)


if __name__ == "__main__":
    num1 = 999999
    num2 = 2

    # Запускаємо функції для знаходження GCD і вимірюємо час виконання
    gcd_subtraction_result, gcd_subtraction_time = gcd_subtraction(num1, num2)
    print(f"GCD by subtraction method: {gcd_subtraction_result}, Time: {
          gcd_subtraction_time} seconds")

    gcd_modulus_result, gcd_modulus_time = gcd_modulus(num1, num2)
    print(f"GCD by modulus method: {gcd_modulus_result}, Time: {
          gcd_modulus_time} seconds")

    gcd_builtin_result, gcd_builtin_time = gcd_builtin(num1, num2)
    print(f"GCD by math gcd method: {
          gcd_builtin_result}, Time: {gcd_builtin_time} seconds")

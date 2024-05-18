import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def first_decorator(func):
    def wrapper():
        try:
            func()
            print("wake up")
        except KeyError:
            pass
    return wrapper

def second_decorator(func):
    def wrapper():
        print("Second in")
        func()
        print("Second out")
    return wrapper

def log_decorator(debug=False):
    def decorator(func):
        def wrapper():
            # запам'ятовує час початку виконання задекорованої функції
            start_time = time.time()
            if debug:
                logger.info(f"Execution started at {start_time}")
            func()
            end_time = time.time()
            if debug:
                logger.info(f"Execution ended at {end_time}")
                logger.info(f"Execution took {end_time - start_time} seconds")
        return wrapper
    return decorator

@log_decorator(debug=False)
def long_function():
    time.sleep(5)
    print("Inside the function")
    raise KeyError

@log_decorator(debug=True)
def other_function():
    time.sleep(2)
    print("Another function")

if __name__ == "__main__":
    long_function()
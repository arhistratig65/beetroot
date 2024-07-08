import logging


class ContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == IndexError:
            logging.error(f'IndexError occurred: {exc_value}')
            return True  # Позначте виняток як оброблений
        else:
            if self.file:
                self.file.close()
            # Дозволити розповсюдження винятків, відмінних від IndexError
            return False

class Rental:
    def __init__(self, property_type, address, num_rooms, rental_price, amenities, available=True):
        # Ініціалізуємо атрибути класу
        self.property_type = property_type  # Тип помешкання
        self.address = address  # Адреса
        self.num_rooms = num_rooms  # Кількість кімнат
        self.rental_price = rental_price  # Вартість оренди за добу
        self.amenities = amenities  # Зручності
        self.available = available  # Доступність для бронювання

    def get_property_info(self):
        # Метод для отримання інформації про помешкання
        return f"Тип помешкання: {self.property_type}, Адреса: {self.address}, " \
               f"Кількість кімнат: {self.num_rooms}, Вартість оренди: {self.rental_price}, " \
               f"Зручності: {', '.join(self.amenities)}, Доступність: {self.available}"

    def book_property(self):
        # Метод для бронювання помешкання
        if self.available:
            self.available = False
            return True
        else:
            return False

    def cancel_booking(self):
        # Метод для скасування бронювання помешкання
        if not self.available:
            self.available = True
            return True
        else:
            return False
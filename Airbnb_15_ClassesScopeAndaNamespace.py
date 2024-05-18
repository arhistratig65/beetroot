from datetime import datetime

class Rental:
    def __init__(self, property_type, address, num_rooms, rental_price, amenities):
        self.property_type = property_type
        self.address = address
        self.num_rooms = num_rooms
        self.rental_price = rental_price
        self.amenities = amenities
        self.bookings = []  # Список бронювань для цього помешкання

    def get_property_info(self):
        return f"Тип помешкання: {self.property_type}, Адреса: {self.address}, " \
               f"Кількість кімнат: {self.num_rooms}, Вартість оренди: {self.rental_price}, " \
               f"Зручності: {', '.join(self.amenities)}"

    def book_property(self, guest_name, start_date, end_date):
        # Перевіряємо доступність помешкання на обрані дати
        for booking in self.bookings:
            if start_date < booking.end_date and end_date > booking.start_date:
                return False  # Якщо помешкання зайняте на обрані дати, повертаємо False

        # Якщо помешкання доступне, створюємо бронювання
        new_booking = Booking(guest_name, self, start_date, end_date)
        self.bookings.append(new_booking)
        return True

class Booking:
    def __init__(self, guest_name, rental_property, start_date, end_date):
        self.guest_name = guest_name
        self.rental_property = rental_property
        self.start_date = start_date
        self.end_date = end_date

    def get_booking_info(self):
        return f"Ім'я гостя: {self.guest_name}, Помешкання: {self.rental_property.address}, " \
               f"Дата початку: {self.start_date}, Дата завершення: {self.end_date}"
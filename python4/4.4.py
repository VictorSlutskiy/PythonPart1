class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.probeg = 0

    def car_info(self):
        return f"{self.make} {self.model} {self.year}"

    def drive(self, km):
        self.probeg += km

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def create_from_string(cls, car_string):
        make, model, year = car_string.split()
        return cls(make, model, int(year))


my_car = Car("Toyota", "Camry", 2022)
print("Моя машина: ", my_car.car_info())
my_car.drive(100000)
my_car.drive(1)
print("Пробег: ", my_car.probeg)
print("2020 - високосный год?", Car.is_leap_year(2020))
car_string = "BMW M5F90 2021"
new_car = Car.create_from_string(car_string)
print("Новая машина: ", new_car.car_info())

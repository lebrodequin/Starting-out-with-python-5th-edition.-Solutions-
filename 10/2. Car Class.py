class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


model_year = input('input year of model: ')
car_make = input('input make of the car: ')
my_car = Car(model_year, car_make, 0)
print(my_car.get_speed())

for i in range(5):
    my_car.accelerate()
    print(my_car.get_speed())

for i in range(5):
    my_car.brake()
    print(my_car.get_speed())

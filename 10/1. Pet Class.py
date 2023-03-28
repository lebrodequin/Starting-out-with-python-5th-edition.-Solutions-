class Pet:
    def __init__(self, pet_name, type_of_animal, age):
        self.__name = pet_name
        self.__type = type_of_animal
        self.__age = age

    def set_name(self, pet_name):
        self.__name = pet_name

    def set_animal_type(self, type_of_animal):
        self.__type = type_of_animal

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__type

    def get_age(self):
        return self.__age


name = input('input animal name: ')
animal_type = input('input animal type: ')
animal_age = input('input animal age: ')

pet1 = Pet(name, animal_type, animal_age)


print(f'{pet1.get_name()}\n'
      f'{pet1.get_animal_type()}\n'
      f'{pet1.get_age()}')

class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phoneNumber = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phoneNumber = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phoneNumber


def main():
    first_person = get_pi()
    second_person = get_pi()
    third_person = get_pi()
    print_pi(first_person)
    print_pi(second_person)
    print_pi(third_person)


def get_pi():
    nm = input('input name: ')
    ad = input('input address: ')
    ag = input('input age: ')
    pn = input('input phone number: ')
    pi = PersonalInformation(nm, ad, ag, pn)
    return pi


def print_pi(pi):
    print(f'{pi.get_name()}\t'
          f'{pi.get_address()}\t'
          f'{pi.get_age()}\t'
          f'{pi.get_phone_number()}')


if __name__ == '__main__':
    main()

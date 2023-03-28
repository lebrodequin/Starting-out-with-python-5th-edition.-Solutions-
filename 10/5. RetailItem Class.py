class RetailItem:
    def __init__(self, descr, units, price):
        self.__description = descr
        self.__units_in_inventory = units
        self.__price = price

    def set_description(self, descr):
        self.__description = descr

    def set_units(self, units):
        self.__units_in_inventory = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    def print_all(self):
        print(f'{self.__description}\t'
              f'{self.__units_in_inventory}\t'
              f'{self.__price}')



item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40, 34.95)
item3 = RetailItem('Shirt', 20, 24.95)
item1.print_all()
item2.print_all()
item3.print_all()
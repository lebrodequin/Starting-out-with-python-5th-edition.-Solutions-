import matplotlib.pyplot as plt


def main():
    expences_list = [50, 50, 60, 40, 20, 30]
    categories_list = ['Rent', 'Gas', 'Food', 'Clothing', 'Car payment', 'Misc']
    plt.pie(expences_list, labels=categories_list)
    plt.title('Expences by categories')
    plt.show()


main()

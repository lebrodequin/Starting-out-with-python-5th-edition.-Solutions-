def main():
    sales = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        x = int(input(f'input the sales for {day}: '))
        sales.append(x)
    print(sales)
    print(sum_list(sales))


def sum_list(list_num):
    total = 0
    for element in list_num:
        total += element
    return total


main()

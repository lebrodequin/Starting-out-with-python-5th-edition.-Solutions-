def main():
    my_string = input('input string: ')
    print(f'the most common character in the string you input is '
          f'{most_common_sym(my_string)}')


def most_common_sym(string):
    sym = string[0].lower()
    counter1 = 0
    counter2 = 0

    for i in range(len(string)):
        for j in range(len(string)):
            if string[i].lower() == string[j].lower():
                counter1 += 1
        if counter1 > counter2:
            counter1 = counter2
            sym = string[i].lower()
    return sym


main()

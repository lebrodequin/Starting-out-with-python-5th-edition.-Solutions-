def main():
    my_string = input('input string: ')
    print(f'The most common symbol in string is {most_common_sym(my_string.lower())}')


def most_common_sym(string):
    # make a list of unique symbols in the string
    string_list = [sym for sym in string]
    string_list = list(dict.fromkeys(string_list))

    index = -1
    max_index = 0
    max_num = 0

    for element in string_list:
        num = string.count(element)
        index += 1

        if num > max_num:
            max_num = num
            max_index = index

    return string_list[max_index]


main()

def main():
    my_string = input('input string: ')
    print(fist_letter_upper(my_string))


def fist_letter_upper(string):
    new_str = string[0].upper()
    for i in range(len(string)):
        if string[i-2] == '.' and string[i-1] == ' ':
            new_str += string[i].upper()
        else:
            new_str += string[i]
    return new_str


if __name__ == '__main__':
    main()

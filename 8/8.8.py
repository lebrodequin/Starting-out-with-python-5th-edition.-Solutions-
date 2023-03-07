def main():
    my_string = input('input string: ')
    print(fist_letter_upper(my_string))


def fist_letter_upper(string):
    for i in range(len(string)):
        if string[i:i+1] == '. ' :
            string.replace([i+2].capitalized)

    return new_str


if __name__ == '__main__':
    main()

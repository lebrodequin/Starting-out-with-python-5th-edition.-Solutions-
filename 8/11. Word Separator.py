def main():
    my_string = input('input string with no spaces: ')
    print(split_into_sentence(my_string))


def split_into_sentence(string):
    new_str = string[0].upper()
    for i in range(1, len(string)):
        if string[i].isupper():
            new_str += ' ' + string[i].lower()
        else:
            new_str += string[i]
    return new_str


main()

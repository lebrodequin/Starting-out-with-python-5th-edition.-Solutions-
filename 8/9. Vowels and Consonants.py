def main():
    my_string = input('please input your string: ')
    print(f'the string you input has {num_of_vowels(my_string)} '
          f'vowels and {num_of_consonants(my_string)} consonants')


def num_of_vowels(string):
    num = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].lower() in ['a', 'e', 'i',
                                     'o', 'u', 'y']:
                num += 1
    return num


def num_of_consonants(string):
    num = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].lower() in ['b', 'c', 'd', 'f',
                                     'g', 'h', 'j', 'k',
                                     'l', 'm', 'n', 'p',
                                     'q', 'r', 's', 't',
                                     'v', 'w', 'x', 'z']:
                num += 1
    return num


main()

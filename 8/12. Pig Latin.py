def main():
    my_string = input('input string: ')
    print(pig_latin_converter(my_string))


def pig_latin_converter(string):
    words = string.split()
    new_words = []
    for word in words:
        new_words.append(word.replace(word[0], '') + 'ay ')
    pig_string = ''.join(word for word in new_words)
    return pig_string.upper()


main()

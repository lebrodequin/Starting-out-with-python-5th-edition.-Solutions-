def main():
    my_str = input('input string, please: ')
    print(my_str.replace('t', 'T'))

'''
def convert_t_to_T(str):
    new_str = ''
    for char in str:
        if char == 't':
            new_str += char.upper()
        new_str += char
    return new_str
'''

if __name__ == '__main__':
    main()
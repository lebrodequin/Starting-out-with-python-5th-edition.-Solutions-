def main():
    my_str = input('input string, please: ')
    print(my_str[::-1])
    print(my_str[0:3])
    print(my_str[-1:-4:-1])

    mystring = 'cookies>milk>fudge>cake>ice cream'
    print(mystring.split('>'))

if __name__ == '__main__':
    main()

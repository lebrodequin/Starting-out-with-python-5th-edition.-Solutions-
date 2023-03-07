def main():
    my_str = input('input string: ')
    print(check_if(my_str))

def check_if(str):
    if str.endswith('.com'):
        return True
    return False

if __name__ == '__main__':
    main()
def main():
    num1 = int(input('input num: '))
    if is_prime(num1) == True:
        print('prime')
    else:
        print('not prime')


def is_prime(x):
    if x % 2 == 0 and x > 3:
        return False
    elif x % 3 == 0 and x >3:
        return False
    else:
        return True


main()


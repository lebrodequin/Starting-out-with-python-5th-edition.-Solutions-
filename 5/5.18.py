def main():
    for y in range(1, 101):
        print(f'{y} is ', end='')
        if is_prime(y):
            print('prime')
        else:
            print('not prime')


def is_prime(x):
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 and x > 3:
        return False
    else:
        return True


main()

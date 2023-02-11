import random


def main():
    evens = 0
    odds = 0
    for x in range(1, 101):
        y = random.randint(1, 100)
        if even_or_odd(y) == 'even':
            evens += 1
        else:
            odds += 1
    print(f'evens {evens}')
    print(f'odds {odds}')


def even_or_odd(num1):
    if num1 % 2 == 0:
        return 'even'
    else:
        return 'odd'


main()

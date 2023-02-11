INCH_IN_FEET = 12


def main():
    feets = float(input('how many feets? '))
    inches = feets_to_inches(feets)
    print(f'its gonna be {inches} inches')


def feets_to_inches(num1):
    x = num1 * INCH_IN_FEET
    return x


main()

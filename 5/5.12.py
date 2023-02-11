def main():
    int1 = int(input('input int1: '))
    int2 = int(input('input int2: '))
    greater_int = greater_of_two(int1, int2)
    print(greater_int)


def greater_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


main()

def main():
    num = int(input('input number: '))
    prime_list = []

    for i in range(2, num+1):
        append = True
        for j in range(2, i):
            if i % j == 0:
                append = False
        if append:
            prime_list.append(i)
    print(prime_list)


main()

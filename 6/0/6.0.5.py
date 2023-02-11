def main():
    total = 0
    file_var = open('numberlist.txt', 'r')
    for i in range(100):
        line = file_var.readline()
        line = int(line.rstrip('\n'))
        total += line
        print(f'{line}')
    file_var.close()
    print(f'total is {total}')


main()
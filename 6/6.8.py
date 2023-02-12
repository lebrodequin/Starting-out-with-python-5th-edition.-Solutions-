def main():
    total = 0
    count = 0
    tempfile = open('random_numbers.txt', 'r')
    num_line = tempfile.readline()
    while num_line != '':
        num_line = int(num_line.rstrip('\n'))
        total += num_line
        count += 1
        num_line = tempfile.readline()
    tempfile.close()
    print(f'total of random numbers is: {total}')
    print(f'totally there are {count} random numbers')


main()

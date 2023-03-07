def main():
    total = 0
    count = 0
    filename = input('input file name: ')
    try:
        tempfile = open(filename, 'r')
        num_line = tempfile.readline()
        while num_line != '':
            num_line = int(num_line.rstrip('\n'))
            total += num_line
            count += 1
            num_line = tempfile.readline()
        avg = total / count
        print(f'the average number is {avg:.2f}')
    except FileNotFoundError:
        print('File not found')
    except IOError:
        print('Incorrect number in file')


main()

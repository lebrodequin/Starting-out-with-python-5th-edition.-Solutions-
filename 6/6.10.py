def main():
    filename = 'golf.txt'
    input_data(filename)
    read_file(filename)


def input_data(file):
    filevar = open(file, 'w')
    keep_going = 'y'
    while keep_going == 'y':
        name = input('input players name: ')
        score = input('input players score: ')
        filevar.write(f'Name:\t {name}\n')
        filevar.write(f'Score:\t {str(score)}\n\n')
        keep_going = input('keep going? (y/n) ')
    filevar.close()


def read_file(file):
    filevar = open(file, 'r')
    line = filevar.readline()
    while line != '':
        line = line.rstrip('\n')
        print(line)
        line = filevar.readline()
    filevar.close()


main()

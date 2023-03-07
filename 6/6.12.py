import random
def main():
#   generate_random()
    calc_avg('steps.txt')


def generate_random():
    tempfile = open('steps.txt', 'w')
    for i in range(365):
        tempfile.write(f'{random.randint(2000,20000)}\n')
    tempfile.close()


def thirty_one_day(filename):
    total = 0
    count = 1
    line = filename.readline()
    for i in range(30):
        line = int(line.rstrip('\n'))
        total += line
        count += 1
        line = filename.readline()
    return total/count


def thirty_days(filename):
    total = 0
    count = 1
    line = filename.readline()
    for i in range(29):
        line = int(line.rstrip('\n'))
        total += line
        count += 1
        line = filename.readline()
    return total/count


def twenty_eight_days(filename):
    total = 0
    count = 0
    line = filename.readline()
    for i in range(27):
        line = int(line.rstrip('\n'))
        total += line
        count += 1
        line = filename.readline()
    return total / count


def calc_avg(filename):
    tempfile = open(filename, 'r')
    print(f'Month:\t\tAverage steps:')
    print(f'January:\t{thirty_one_day(tempfile):.0f}')
    print(f'February:\t{twenty_eight_days(tempfile):.0f}')
    print(f'March:\t\t{thirty_one_day(tempfile):.0f}')
    print(f'April:\t\t{thirty_days(tempfile):.0f}')
    print(f'May:\t\t{thirty_one_day(tempfile):.0f}')
    print(f'June:\t\t{thirty_days(tempfile):.0f}')
    print(f'July:\t\t{thirty_one_day(tempfile):.0f}')
    print(f'August:\t\t{thirty_one_day(tempfile):.0f}')
    print(f'September:\t{thirty_days(tempfile):.0f}')
    print(f'October:\t{thirty_one_day(tempfile):.0f}')
    print(f'November:\t{thirty_days(tempfile):.0f}')
    print(f'December:\t{thirty_one_day(tempfile):.0f}')
    tempfile.close()


main()

def main():
    winnwers_list = make_list_from_file('WorldSeriesWinners.txt')
    years = []
    year = 1903
    for i in range(len(winnwers_list)):
        years.append(year)
        year += 1
    print('Year\tWinner')
    for i in range(len(winnwers_list)):
        print(f'{years[i]}\t', end='')
        print(f'{winnwers_list[i]}\t\t')

    team = input('input the team name: ')
    print(f'this team wor {how_many_times_str_in_list(winnwers_list, team)} times')

def how_many_times_str_in_list(list, str):
    counter = 0
    for i in range(len(list)):
        if str == list[i]:
            counter +=1
    return counter


def make_list_from_file(filename):
    list1 = []
    var_file = open(filename, 'r')
    line = var_file.readline()
    while line != '':
        line = line.rstrip('\n')
        list1.append(line)
        line = var_file.readline()
    var_file.close()
    return list1

main()

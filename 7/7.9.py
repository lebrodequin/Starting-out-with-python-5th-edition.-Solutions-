def main():
    population_dynamics = make_list_from_file('USPopulation.txt')
    years = []
    current_year = 1950
    for i in range(len(population_dynamics)):
        years.append(current_year)
        current_year += 1

    annual_change_list = [0,]
    for i in range(len(population_dynamics)-1):
        value = population_dynamics[i+1]-population_dynamics[i]
        annual_change_list.append(value)

    print('year\tpopulation\tchange')
    for i in range(len(population_dynamics)):
        print(f'{years[i]}\t', end='')
        print(f'{population_dynamics[i]}\t\t', end='')
        print(f'{annual_change_list[i]}')
    print(f'average change for all the time is {average(annual_change_list):.0f}')
    print(f'greatest increase is {max(annual_change_list)}')
    print(f'the smallest increase is {min(annual_change_list[1:])}')

def average(list):
    count = 0
    total = 0
    for i in list:
        count += 1
        total += i
    avg = total/count
    return avg


def make_list_from_file(filename):
    list1 = []
    var_file = open(filename, 'r')
    line = var_file.readline()
    while line != '':
        line = int(line.rstrip('\n'))
        list1.append(line)
        line = var_file.readline()
    var_file.close()
    return list1

main()

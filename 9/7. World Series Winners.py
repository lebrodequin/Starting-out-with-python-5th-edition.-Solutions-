def main():
    filename = 'worldseries.txt'
    list_of_winners = line_2_list(filename)
    list_of_winners.insert(1, 'World Series was not played')
    list_of_winners.insert(91, 'World Series was not played')

    list_of_years = []
    for year in range(1903, 2010):
        list_of_years.append(year)

    winners_dict = {}
    for i in range(107):
        winners_dict[list_of_years[i]] = list_of_winners[i]

    number_of_wins_dict = {}
    for team in set(list_of_winners):
        counter = 0
        for i in range(len(list_of_winners)):
            if team == list_of_winners[i]:
                counter +=1
        number_of_wins_dict[team] = counter
    print(number_of_wins_dict)

    my_year = int(input('input year number(1903-2009): '))
    print(f'in the year {my_year} the {winners_dict.get(my_year)} won the World Series\n'
          f'since 1903 till 2009 {winners_dict.get(my_year)} won {number_of_wins_dict.get(winners_dict.get(my_year))} times')


def line_2_list(filename):
    file_var = open(filename, 'r')
    line = file_var.readline()
    line_list = []
    while line != '':
        line = line.rstrip('\n')
        line_list.append(line)
        line = file_var.readline()
    return line_list


main()

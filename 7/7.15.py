def main():
    week_num_list = []
    price_list = make_list_from_file('1994_Weekly_ Gas_Averages.txt')
    for i in range(1, len(price_list)+1):
        week_num_list.append(i)
    print(week_num_list)




def make_list_from_file(filename):
    list1 = []
    var_file = open(filename, 'r')
    line = var_file.readline()
    while line != '':
        line = float(line.rstrip('\n'))
        list1.append(line)
        line = var_file.readline()
    var_file.close()
    return list1

main()
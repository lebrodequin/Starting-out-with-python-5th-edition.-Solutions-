def main():
    boys_names = make_list_from_file('BoyNames.txt')
    girls_names = make_list_from_file('GirlNames.txt')

    x = input('would you like to search for boys name (y/n):')
    if x == 'y':
        name = input('input name: ')
        if check_if_str_in_list(boys_names, name):
            print('yes')
        else:
            print('no')


    x = input('would you like to search for girls name (y/n):')
    if x == 'y':
        name = input('input name: ')
        if check_if_str_in_list(girls_names, name):
            print('yes')
        else:
            print('no')


def check_if_str_in_list(list, str):
    if str in list:
        return True
    else:
        return False


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
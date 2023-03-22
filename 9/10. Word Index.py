def main():
    file_var = open('kennedy.txt', 'r')
    line = file_var.readline()
    my_list_2d = []
    my_list_1d = []
    while line != '':
        line = line.rstrip('\n')
        line_list = line.split()
        my_list_2d.append(line.split())
        for i in range(len(line_list)):
            my_list_1d.append(line_list[i])
        line = file_var.readline()
    my_set = set(my_list_1d)
    file_var.close()

    my_dict = {}
    for word in my_set:
        my_list = []
        for numline in range(len(my_list_2d)):
            for elem in my_list_2d[numline]:
                if word == elem:
                    my_list.append(numline+1)
        my_dict[word] = set(my_list)

    out_file = open('index.txt', 'w')
    for key in my_dict.keys():
        out_file.write(f'{key}: \t\t{my_dict.get(key)}\n')
    out_file.close()


main()

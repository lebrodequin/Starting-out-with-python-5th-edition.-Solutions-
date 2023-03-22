def main():
    file_var = open('pbnumbers.txt', 'r')
    matrix_list = []
    line = file_var.readline()
    while line != '':
        line = line.rstrip('\n')
        line_list = line.split()
        matrix_list.append(line_list)
        line = file_var.readline()
    file_var.close()

    lottery_list = []
    for i in range(len(matrix_list)):
        for j in range(5):
            lottery_list.append(matrix_list[i][j])

    powerball_list = []
    for i in range(len(matrix_list)):
        powerball_list.append(matrix_list[i][5])

    print(frequency(lottery_list, 69))
    print(frequency(powerball_list, 26))

    ten_most_frequent(frequency(lottery_list, 69))


def frequency(list, length):
    freq_dict = {}
    for i in range(1, length+1):
        counter = 0
        for j in list:
            if i == int(j):
                counter += 1
        freq_dict[i] = counter
    return freq_dict


def ten_most_frequent(dictionary):
    ten_dict = {}
    for i in range(10):
        freq_list = list.sort(dictionary.values())
        print(max(freq_list))

main()

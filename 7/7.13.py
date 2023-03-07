import random


def main():
    remain_asking = 'y'
    answers_list = make_list_from_file('8_ball_responses.txt')
    while remain_asking == 'y':
        input('ask me yes or no question? ')
        print(answers_list[random.randint(1, 12)])
        remain_asking = input('have any other questions? (y/n): ')


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

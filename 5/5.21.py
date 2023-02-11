import random


def main():
    keep_going = True
    while keep_going:
        computer_choice = random.randint(1, 3)
        human_choice = rps_input()
        print(f'computer chose {computer_choice_str(computer_choice)}')
        print(f'so the result is: {result(computer_choice, human_choice)}')
        if computer_choice != human_choice:
            keep_going = False


def rps_input():
    continue_input = True
    while continue_input:
        str1 = input('rock, paper of scissors: ')
        if str1 == 'rock':
            return 1
        elif str1 == 'paper':
            return 2
        elif str1 == 'scissors':
            return 3
        else:
            print('incorrect input, please try again')
            continue_input = True


def computer_choice_str(x):
    if x == 1:
        return 'rock'
    elif x == 2:
        return 'paper'
    else:
        return 'scissors'


def result(cc, hc):
    if cc == hc:
        return 'draw. please try again'
    elif (cc == 1 and hc == 3 or
          cc == 2 and hc == 1 or
          cc == 3 and hc == 2):
        return 'computer wins'
    else:
        return 'you win'


main()

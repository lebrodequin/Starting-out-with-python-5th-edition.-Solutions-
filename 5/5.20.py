import random


def main():
    keep_going = True
    ran_num = random.randint(1, 100)
    print(ran_num)

    while keep_going:
        num1 = inputnum()
        keep_going = still_keep_going(num1, ran_num)
        print(f'{check(num1, ran_num)}')

def inputnum():
    inp_num = int(input('input number from 1 to 100: '))
    while inp_num < 1 or inp_num > 100:
        inp_num = int(input('ERROR. It must be from 1 to 100: '))
    return inp_num

def check(x, y):
    if x > y:
        return 'the input num is too high'
    elif x < y:
        return 'the input num is too low'
    else:
        return 'congrats you win'

def still_keep_going(x, y):
    if x != y:
        return True
    else:
        return False

main()

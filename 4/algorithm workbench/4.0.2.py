repeat = 'y'
while repeat == 'y' or repeat == 'Y':
    num1 = float(input('input number 1 '))
    num2 = float(input('input number 2 '))
    sum1_2 = num1 + num2
    print(f'sum of input numbers is {sum1_2:.0f}')
    repeat = str(input('would you like to repeat? (y/n) '))

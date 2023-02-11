budg = float(input('input the amount of money for this months: '))
total_exp = 0
run = 'y'

while run == 'y':
    expence = float(input('how much have you spent? '))
    total_exp += expence
    run = input('any other expenses? (y/n) ')

if budg >= total_exp:
    print('your in budget')
else:
    print('you are out of budget')

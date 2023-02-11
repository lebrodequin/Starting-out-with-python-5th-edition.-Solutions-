first_color = str(input('input first basic color (red, blue or yellow)\n'))
second_color = str(input('input second basic color (red, blue or yellow)\n'))

if first_color != 'red' and first_color != 'blue' and first_color != 'yellow' and second_color != 'red' and second_color != 'blue' and second_color != 'yellow':
    print('the input is incorrect')
if first_color == 'red' and second_color == 'blue' or first_color == 'blue' and second_color == 'red':
    print('purple')
if first_color == 'red' and second_color == 'yellow' or first_color == 'yellow' and second_color == 'red':
    print('orange')
if first_color == 'blue' and second_color == 'yellow' or first_color == 'yellow' and second_color == 'blue':
    print('green')
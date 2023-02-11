SUGAR_1COOKIE = 1.5 / 48
BUTTER_1COOKIE = 1 / 48
FLOUR_1COOKIE = 2.75 / 48
num_of_cookies = float ( input( 'how many cookies would you like to bake? '))
sugar_for_cook = num_of_cookies * SUGAR_1COOKIE
butter_for_cook = num_of_cookies * BUTTER_1COOKIE
flour_for_cook = num_of_cookies * FLOUR_1COOKIE
print(
    f'for thsi purpose you will need\n'+
    f'{sugar_for_cook:.2f} cups of sugar\n'+
    f'{butter_for_cook:.2f} cups of butter\n'+
    f'{flour_for_cook:.2f} cups of flour'
     )
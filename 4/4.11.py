KG_IN_POUND = 0.453592

weight = float(input('input your weight (kg): '))

print('if you cut 500 calories at a day your weight would change in the following way: ')

for x in range(1,7,1):
    weight -= 4*KG_IN_POUND
    print(f'at the end of the {x} month your weight would be {weight:.0f} pounds')

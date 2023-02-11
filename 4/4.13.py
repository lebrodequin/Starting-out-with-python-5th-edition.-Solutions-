start_num = int(input('input starting number of organisms '))
avg_increase = float(input('input average daily increase of organisms, % '))
days = int(input('for how many days would that happen? '))

print('Day Approximate\t\tPopulation')
for x in range(1, days+1, 1):
    print(f'{x}\t\t\t\t\t{start_num:.0f}')
    start_num *= (100+avg_increase)/100
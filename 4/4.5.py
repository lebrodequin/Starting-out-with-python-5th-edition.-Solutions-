#number of years
ny = int(input('input the number of years: '))
#rainfall in inches total
rf_total = 0.0
#number of months
mn = 0

for x in range(ny):
    for y in range(1,13,1):
        rf = float(input(f'how many inch. of rainfall did you had in the {x} year in the {y} month '))
        rf_total += rf
        mn += 1
avg = rf_total / mn
print(f'number of month: {mn:.0f}\n'
      f'total inches: {rf_total:.2f}\n'
      f'average per month: {avg:.2f}')
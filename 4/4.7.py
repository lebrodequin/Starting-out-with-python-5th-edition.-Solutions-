# the number of days
nd = int(input('input the number of days '))
# total salary
total = 0
salary = 1

for x in range (nd):
    salary_usd = salary / 100
    total += salary
    salary *= 2
    print(f'{x+1} day you\'ve earned ${salary_usd:.2f}')
total_usd = total / 100
print(f'TOTAL: ${total_usd}')
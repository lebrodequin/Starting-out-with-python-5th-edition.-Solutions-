bugs_total = 0

for day in [1, 2, 3, 4, 5]:
    bugs = int(input(f'how many bugs have you collected on {day} day '))
    bugs_total += bugs
print(f'totally you have got {bugs_total} bugs')

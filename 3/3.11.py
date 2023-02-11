num = int(input('input a number of books purchased last month\n'))
if num >= 8:
    point = 60
elif num >= 6:
    point = 30
elif num >= 4:
    point = 15
elif num >= 2:
    point = 5
else:
    point = 0

print(f'You got {point} points this month')

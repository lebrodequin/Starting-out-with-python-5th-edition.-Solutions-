year = int(input('enter a year:\n'))
if year % 100 == 0 and year % 400 == 0 or year % 4 == 0:
    days = 29
else:
    days = 28
print (f'In {year} February has {days} days')

date = int(input('input date\n'))
month = int(input('input month\n'))
year = int(input('input year (last two digits)\n'))

if date * month == year:
    print ('your date of birth is magic')
else:
    print('your date of birth is not magic')
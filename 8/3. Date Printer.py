date_raw = input('input date mm/dd/yyyy: ')
date = date_raw.split('/')

month = int(date[0])
month_str = ['January',     'February',     'March', 
             'April',       'May',          'June',
             'July',        'August',       'September',
             'October',     'Novermber',    'December']
day = date[1]
year = date[2]

print(f'{month_str[month-1]} {day}, {year}')

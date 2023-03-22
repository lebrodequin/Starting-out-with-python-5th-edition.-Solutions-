def main():
    months = ['jan', 'feb', 'mar',
              'apr', 'may', 'jun',
              'jul', 'aug', 'sep',
              'okt', 'nov', 'dec']
    rainfall_list = []

    for month in months:
        x = int(input(f'input the value of rainfall in {month}: '))
        rainfall_list.append(x)

    print(f'max value is        {max(rainfall_list)}\n'
          f'min value is        {min(rainfall_list)}\n'
          f'average value is    {average(rainfall_list) :.2f}')


def average(list1):
    count = 0
    total = 0
    for i in list1:
        count += 1
        total += i
    avg = total/count
    return avg


main()

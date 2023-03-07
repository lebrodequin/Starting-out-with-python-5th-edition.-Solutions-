def main():
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']
    list1 = []

    for mon in months:
        x = int(input(f'input the value of rainfall in {mon}: '))
        list1.append(x)

    print(list1)
    print(f'max value is {max(list1)}')
    print(f'min value is {min(list1)}')
    print(f'average value is {average(list1):.2f}')

def average(list):
    count = 0
    total = 0
    for i in list:
        count += 1
        total += i
    avg = total/count
    return avg

main()
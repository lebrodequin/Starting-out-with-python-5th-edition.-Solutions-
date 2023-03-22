def main():
    list1 = []
    for num in range(20):
        x = int(input(f'input the value: '))
        list1.append(x)

    print(list1)
    print(f'max value is                {max(list1)}'
          f'min value is                {min(list1)}'
          f'total numbers in list is    {len(list1)}'
          f'average value is            {average(list1):.2f}')


def average(list1):
    count = 0
    total = 0
    for i in list1:
        count += 1
        total += i
    avg = total/count
    return avg


main()

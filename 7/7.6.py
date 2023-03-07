def main():
    list1 = [100, 10, 299, 45, 11, 32, 124, 35, 654, 43]
    print(list1)
    num = int(input('input num: '))
    print(f'here are all the elements that are greater than {num}: {if_larger(list1, num)}')


def if_larger(list1, num):
    greater_list = []
    for element in list1:
        if element > num:
            greater_list.append(element)
    return greater_list


main()

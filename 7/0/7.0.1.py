my_list = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
print(my_list)

for i in my_list:
    print(i)

list1 = [1, 2, 3, 4, 5, 6]
list2 = []
list2 = list2 + list1
print(list2)

def sum1(list_no):
    total = 0
    for i in list_no:
        total +=i
    return total

print(sum1(list2))

names = ['Ivan', 'Ruby', 'Karl']
if 'Ruby' in names:
    print('yes')
else:
    print('no')
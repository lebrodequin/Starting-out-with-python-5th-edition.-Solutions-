'''
my_dict1 = {'a': 1, 'b' : 2, 'c' : 3}
print(type(my_dict1))
print(my_dict1)

my_dict2 = {}
print(type(my_dict1))
print(my_dict2)

dct = {'James' : 35, 'Ivan' : 33, 'Jim': 23}
print(dct)
name = input('input name: ')
print(dct.get(name, 'Not found'))

if name in dct.keys():
    print('gooo')
else:
    print('not goo')

dct.pop(name, 'not found')
print(dct)

my_set1 = {0, 20, 30, 40, 50, 60}
my_set2 = {50, 60, 70, 80, 90, 100}

print(my_set1.union(my_set2))

my_set3 = my_set1.union(my_set2)
print(my_set3)

my_set4 = my_set1.intersection(my_set2)
print(my_set4)

my_set5 = my_set1.difference(my_set2)
print(my_set5)

my_set6 = my_set2.difference(my_set1)
print(my_set6)

my_set7 = my_set1.symmetric_difference(my_set2)
print(my_set7)
'''

my_list = [1, 2, 3, 4, 5]
my_dict = {}
for i in my_list:
    my_dict[i] = i * 10
print(my_dict)

test_averages = {'Janelle': 98,
                 'Sam': 87,
                 'Jennifer': 92,
                 'Thomas': 74,
                 'Sally': 89,
                 'Zeb': 84
                 }

high_scores = {k:v for k, v in test_averages.items() if v > 90}
print(high_scores)
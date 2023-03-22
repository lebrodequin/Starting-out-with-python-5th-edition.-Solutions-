import random
random_list = []
for i in range(7):
    random_list.append(random.randint(1, 9))
for i in random_list:
    print(i, end=' ')

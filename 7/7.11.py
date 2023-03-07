magic_list =[[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print(magic_list)

sum = 0
for y in range(3):
    for x in range(3):
        sum += magic_list[y][x]
    print(f'sum of line {y+1} is {sum}')
    sum = 0

for x in range(3):
    sum += magic_list[x][x]
print(f'sum of slash diagonal is {sum}')
sum = 0

for x in range(2, -1, -1):
    sum += magic_list[x][x]
print(f'sum of backslash diagonal is {sum}')
sum = 0


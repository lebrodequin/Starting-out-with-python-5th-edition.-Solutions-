count_spaces = 0
count_num = 0
count_low = 0
mystring = input('input random string: ')
for i in mystring:
    if i == ' ':
        count_spaces += 1
for i in mystring:
    if i.isdigit():
        count_num += 1
for i in mystring:
    if i.islower():
        count_low += 1


print(f'you have {count_spaces} spaces in string')
print(f'you have {count_num} digits in string')
print(f'you have {count_low} lowercase symbols in string')
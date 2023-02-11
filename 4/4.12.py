num = int(input('input non-negative int: '))
factorial = 1

while num <= 0:
    num = int(input('the number must be positive and >=1, input again: '))

for x in range (1, num+1, 1):
    factorial *= x
print(f'factorial of {num} is {factorial}')

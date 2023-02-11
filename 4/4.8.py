# input the number
num = float(input('input the positive number: '))
total = 0.0

while num >= 0:
    total += num
    num = float(input('input another positive number: '))
print(f'sum of the all positive numbers equal {total:.0f}')

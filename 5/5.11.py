import random
x = random.randint(1, 200)
y = random.randint(1, 200)

print(x)
print(y)

z = int(input('enter the sum of the above numbers '))
while z != x + y:
    z= int(input('try to input once again: '))
print('you win!!!')
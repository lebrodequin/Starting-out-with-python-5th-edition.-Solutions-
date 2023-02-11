speed = float(input('what is the speed? '))
time = int(input('how many hours? '))
distance = 0

print('Hour\tDistance travelled')
print('___________________________________')
for hour in range(1, time+1, 1):
    distance = speed * hour
    print(f'{hour}\t\t{distance:.0f}')

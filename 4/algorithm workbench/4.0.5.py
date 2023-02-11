total = 0.0
numerator = 0
denominator = 31
for x in range(30):
    numerator += 1
    denominator -=1
    print(numerator)
    print(denominator)
    total += numerator/denominator
print(f'{total:.4f}')

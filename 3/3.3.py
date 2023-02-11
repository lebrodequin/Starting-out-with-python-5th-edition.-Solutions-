age = float(input('whats your age?\n'))

if age < 0 or age > 100:
    print('input correct value')
elif age <= 1:
    print('you are infant')
elif 1 < age < 13:
    print('you are a child')
elif 13 <= age < 20:
    print('you are a teenager')
elif age >= 20:
    print('you are an adult')

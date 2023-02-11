RISING_LEVEL = 1.6
total = 0

for x in range (1, 26, 1):
    total += RISING_LEVEL
    print(f'{x} year the level would increase on {total:.2f} mm')
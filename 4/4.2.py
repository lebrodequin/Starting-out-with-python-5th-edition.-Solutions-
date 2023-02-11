CAL_PER_MIN = 4.2

for min in range(10, 31, 5):
    callories_burned = min*CAL_PER_MIN
    print(f'in {min} minutes you have burned {callories_burned} callories')
SEC_IN_MIN = 60
SEC_IN_HOUR = 3600
SEC_IN_DAY = 86400

seconds = int(input('input the number of seconds\n'))
day = 0
hour = 0
minut = 0

if seconds >= SEC_IN_DAY:
    day = seconds // SEC_IN_DAY
    hour = (seconds % SEC_IN_DAY) // SEC_IN_HOUR
    minut = (seconds % SEC_IN_HOUR) // SEC_IN_MIN
    seconds = seconds % SEC_IN_MIN
elif seconds >= SEC_IN_HOUR:
    hour = seconds // SEC_IN_HOUR
    minut = (seconds % SEC_IN_HOUR) // SEC_IN_MIN
    seconds = seconds % SEC_IN_MIN
elif seconds >= SEC_IN_MIN:
    minut = seconds // SEC_IN_MIN
    seconds = seconds % SEC_IN_MIN
print(f'it is {day} days {hour} hours {minut} minutes {seconds} seconds')
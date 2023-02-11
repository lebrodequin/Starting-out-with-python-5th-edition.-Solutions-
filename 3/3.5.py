mass = float(input('input mass, kg\n'))
weight = mass * 9.8
if weight > 500:
    print('its too heavy')
elif weight < 100:
    print('its too light')
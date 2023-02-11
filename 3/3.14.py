weight = float(input('input your weight, kg\n'))
height = float(input('input your height, m\n'))
bmi = weight / (height ** 2)
if 18.5 > bmi:
    print('you are underweighted')
elif 18.5 <= bmi < 25:
    print('your weight is optimal')
elif bmi > 25:
    print('you are overweighted')

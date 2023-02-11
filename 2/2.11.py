num_males = float(input('input number of males: '))
num_female = float(input('input number of females: '))
percent_of_males = (num_males / (num_males + num_female)) * 100
percent_of_females = (num_female / (num_males + num_female)) * 100
print(
    f'you have {percent_of_males:.2f}% of males in your class\n'
    f'and you have {percent_of_females:.2f}% of females in your class'
)

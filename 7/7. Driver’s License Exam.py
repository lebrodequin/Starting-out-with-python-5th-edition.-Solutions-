correct_answers = ['A', 'C', 'A', 'A',
                   'D', 'B', 'C', 'A',
                   'C', 'B', 'A', 'D',
                   'C', 'A', 'D', 'C',
                   'B', 'B', 'D', 'A']
real_answers = []

file_var = open('answers.txt', 'r')
line = file_var.readline()
while line != '':
    line = line.rstrip('\n')
    real_answers.append(line)
    line = file_var.readline()
file_var.close()

print(correct_answers)
print(real_answers)

counter_correct = 0
counter_incorrect = 0
list_of_incorrect_numbers = []

for i in range(len(correct_answers)):
    if real_answers[i] == correct_answers[i]:
        counter_correct += 1
    else:
        counter_incorrect += 1
        list_of_incorrect_numbers.append(i+1)

if counter_correct >= 15:
    print('you passed the exam')
else:
    print('you have failed the exam')

print(f'the number of correct answers is: {counter_correct}')
print(f'the number of incorrect answers is: {counter_incorrect}')
print(f'here are incorrect answers question numbers - {list_of_incorrect_numbers}')

continue_input = True
while continue_input:
    my_number = str(input('input number: '))
    if my_number.isdigit():
        continue_input = False

my_sum = 0
for digit in my_number:
    digit = int(digit)
    my_sum += digit
print(my_sum)

def main():
    num_upper = 0
    num_lower = 0
    num_digit = 0
    num_white = 0

    file_var = open('text.txt', 'r')
    line = file_var.readline()
    while line != '':
        for sym in line:
            if sym.isupper():
                num_upper += 1
            elif sym.islower():
                num_lower += 1
            elif sym.isdigit():
                num_digit += 1
            elif sym == ' ':
                num_white += 1
        line = file_var.readline()
    file_var.close()

    print(f'num of uppercase letter is  {num_upper}\n'
          f'num of lowercase letter is  {num_lower}\n'
          f'num of digits is            {num_digit}\n'
          f'num of whitespaces is       {num_white}')


main()

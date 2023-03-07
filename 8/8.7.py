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
                num_digit +=1
            elif sym == ' ':
                num_white += 1
        line = file_var.readline()
    file_var.close()

    print(f'num of uppercase letter is  {num_upper}')
    print(f'num of lowercase letter is  {num_lower}')
    print(f'num of digits is            {num_digit}')
    print(f'num of whitespaces is       {num_white}')

if __name__ == '__main__':
    main()

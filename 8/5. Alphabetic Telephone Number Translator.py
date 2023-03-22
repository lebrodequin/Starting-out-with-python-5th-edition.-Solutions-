def main():
    phone_num = input('input phone num XXX-XXX-XXXX: ')
    print(convert_phone_to_digits(phone_num))


def convert_phone_to_digits(str_num):
    phone_num_digit = ''
    for sym in str_num:
        if sym.isdigit() or sym == '-':
            phone_num_digit += str(sym)
        elif sym.upper() == 'A' or 'B' or 'C':
            phone_num_digit += '2'
        elif sym.upper() == 'D' or 'E' or 'F':
            phone_num_digit += '3'
        elif sym.upper() == 'J' or 'K' or 'L':
            phone_num_digit += '4'
        elif sym.upper() == 'M' or 'N' or 'O':
            phone_num_digit += '5'
        elif sym.upper() == 'P' or 'Q' or 'R' or 'S':
            phone_num_digit += '6'
        elif sym.upper() == 'T' or 'U' or 'V':
            phone_num_digit += '7'
        elif sym.upper() == 'W' or 'X' or 'Y' or 'Z':
            phone_num_digit += '8'

    print(phone_num_digit)


main()

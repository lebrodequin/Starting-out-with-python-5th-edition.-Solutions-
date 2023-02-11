def main():
    quan_a = int(input('how many A class tickets have been sold? '))
    quan_b = int(input('how many B class tickets have been sold? '))
    quan_c = int(input('how many C class tickets have been sold? '))
    x = revenue(quan_a, quan_b, quan_c)
    print(f'the revenue for tickets is $ {x}')


def revenue(a, b, c):
    rev_a = a * 20
    rev_b = b * 15
    rev_c = c * 10
    rev = rev_a + rev_b + rev_c
    return rev


main()

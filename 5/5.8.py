def main():
    sq_feet = float(input('how many feets? '))
    gal_price = float(input('how much is one gallon? '))
    ng = num_of_gal(sq_feet)
    hr = hours_required(sq_feet)
    cp = cost_of_paint(ng, gal_price)
    lc = labor_charges(hr)
    tc = cp + lc

    print(f'you will require {ng:.2f} gallons of paint')
    print(f'and {hr:.1f} hours of labour')
    print(f'the paint would cost you $ {cp:.2f}')
    print(f'the labour would cost you $ {lc:.2f}')
    print(f'total cost of job is $ {tc:.2f}')


def num_of_gal(num1):
    x = num1 / 112
    return x


def hours_required(num1):
    x = num1 / 112 * 8
    return x


def cost_of_paint(num1, num2):
    x = num1 * num2
    return x


def labor_charges(num1):
    x = num1 * 35
    return x


main()

STATE_TAX = 0.05        # 5%
COUNTRY_TAX = 0.025     # 2.5%


def main():
    sales_amount = float(input('input sales amount: '))
    ct = country_sales_tax(sales_amount)
    st = state_sales_tax(sales_amount)
    tt = total_sales_tax(ct, st)

    print(f'the amount of country sales tax is $ {ct}')
    print(f'the amount of state sales tax is $ {st}')
    print(f'the amount of total sales tax is $ {tt}')


def country_sales_tax(num1):
    x = num1 * COUNTRY_TAX
    return x


def state_sales_tax(num1):
    x = num1 * STATE_TAX
    return x


def total_sales_tax(num1, num2):
    x = num1 + num2
    return x


main()

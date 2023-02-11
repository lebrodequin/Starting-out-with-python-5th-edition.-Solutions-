def main():
    purchase_amount = float(input('input the amount of purchase '))
    print('purchase amount ', purchase_amount)
    print('state sales tax ', state_tax(purchase_amount))
    print('country sales tax ', country_tax(purchase_amount))
    print('total sales tax ', total_tax(purchase_amount))
    print('total ', total(purchase_amount))

def state_tax(sum1):
    return sum1 * 0.05

def country_tax(sum1):
    return sum1 * 0.025

def total_tax(sum1):
    return sum1 * (0.05 + 0.025)

def total(sum1):
    return sum1 * (1 + 0.05 + 0.025)

main()

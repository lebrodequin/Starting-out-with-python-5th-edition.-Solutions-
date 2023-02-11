def main():
    amount = float(input('input amount of cost of a house '))
    min_ins = minimal_insurance_amount(amount)
    print(f'the minimal insurance amount for your house is ${min_ins}')

def minimal_insurance_amount(sum1):
    return sum1 * 0.8

main()

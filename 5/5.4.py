def main():
    loan_payment = float(input('input the monthly costs for loan payment: '))
    insutance = float(input('input the monthly costs for insurance: '))
    gas = float(input('input the monthly costs for gas: '))
    oil = float(input('input the monthly costs for oil: '))
    tyres = float(input('input the monthly costs for tyres: '))
    maintenance = float(input('input the monthly costs for maintenance: '))
    mt = monthly_total(loan_payment, insutance, gas, oil, tyres, maintenance)
    yt = mt * 12 #yearly total
    print(f'the monthly cost for a car is $ {mt}')
    print(f'the yearly cost for a car is $ {yt}')

def monthly_total(num1, num2, num3, num4, num5, num6):
    return num1 + num2 + num3 + num4 + num5 + num6

main()
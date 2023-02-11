def main():
    acres = float(input('how much is your property? '))
    x = property_tax(acres)
    print(f'you will pay $ {x:.2f} taxes')
def property_tax(val1):
    sum1 = val1*0.6*0.0072
    return sum1
main()
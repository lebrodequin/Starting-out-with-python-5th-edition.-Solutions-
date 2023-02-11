def main():
    present_value = float(input('input present value, $: '))
    interest_rate = float(input('input monthly interest rate, %: '))
    num_of_month = float(input('input number of month: '))
    print(f'you will get $ {future_value(present_value, interest_rate, num_of_month):.2f}')

def future_value(p, i, t):
    f = p * (1 + i/100) ** t
    return f

main()

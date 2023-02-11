deposit_amount = float(input('input deposit amount, USD: '))
interest_rate = float(input('input the annual interest rate, %: '))
comp_interest_yearly = float(input('how many times a year the interest is compounded, times: '))
num_of_years = float(input('input the number of years of deposit, years: '))

final_amount = deposit_amount*((1+(interest_rate / 100 / comp_interest_yearly))**(comp_interest_yearly * num_of_years))
print(
    f'you will get {final_amount:,.2f} USD after all this shit'
)

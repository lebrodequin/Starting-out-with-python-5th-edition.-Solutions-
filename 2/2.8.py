price_of_a_meal = float ( input ('how  much is the food? '))
tip = price_of_a_meal * 0.18
tax = price_of_a_meal * 0.07
print (
    f'the price of a \'meal\' is:\t {price_of_a_meal:>20e}\n' +
    f'tip is:\t\t\t\t {tip:>20.2e}\n' +
    f'tax is:\t\t\t\t {tax:>20.2f}\n' +
    f'total is:\t\t\t {price_of_a_meal+tip+tax:>20.2f}\n'
      )

#[alignment][width][,][.precision][type]
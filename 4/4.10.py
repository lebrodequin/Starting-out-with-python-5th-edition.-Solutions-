tuition_price = 8000
total = 0.0
PRICE_INCREACE = 0.03

for x in range(1,6,1):
    for y in range(1,3,1):
        total += tuition_price
        tuition_price *= (1+PRICE_INCREACE)
        print(f'the price for {x} year {y} semester is {tuition_price:.0f}')
print(f'total price for education is {total:.0f}')
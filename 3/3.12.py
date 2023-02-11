PRICE = 99
num = int(input('how many packages do you buy?\n'))
if num >= 100:
    discount = 0.4
elif 50 <= num <= 99:
    discount = 0.3
elif 20 <= num <= 49:
    discount = 0.2
elif 10 <= num <= 19:
    discount = 0.2
else:
    discount = 0

if discount != 0:
    discount_amount = PRICE * num * discount
    print(f'the amount of discount is {discount_amount} USD')

total_amount = PRICE * num - PRICE * num * discount
print(f'the total amount of your purchase is {total_amount} USD')
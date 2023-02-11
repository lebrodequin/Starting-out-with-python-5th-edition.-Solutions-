weight = float(input('input weight, pounds \n'))
if weight <= 2:
    rate = 1.5
elif 2 < weight <= 6:
    rate = 3
elif 6 < weight <=10:
    rate = 4
elif weight >= 10:
    rate = 4.75

shipping_charges = weight * rate
print(f'shipping charges costs {shipping_charges} USD')
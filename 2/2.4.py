bread_price = float (input ( 'input bread price ' ) ) #запрос цены хлеба
sour_cream_price = float ( input ( 'input sour crea price ' ) )
chips_price = float ( input ( 'input chips price ') )
ketchup_price = float ( input ( 'input kettchup price ') )
mayo_price = float ( input ( 'input mayo price ') )
subtotal = bread_price + sour_cream_price + chips_price + ketchup_price + mayo_price
tax = subtotal * .07
total = subtotal + tax
print ('subtotal: ', subtotal)
print ('tax: ',tax)
print ('total: ', total)
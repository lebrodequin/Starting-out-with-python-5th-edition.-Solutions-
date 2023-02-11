purchase_amount = float ( input ('input the amount of purchase '))
state_tax = purchase_amount * 0.05
country_tax = purchase_amount * 0.025
total_tax = state_tax + country_tax
total = purchase_amount + total_tax


print ('purchase amount ',purchase_amount)
print ('state sales tax ', state_tax)
print ('country sales tax ', country_tax)
print ('total sales tax ', total_tax)
print ('total ',total)
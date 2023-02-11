NUMBER_OF_SHARES = 2000
PURCHASE_PRICE = 40.0
SELL_PRICE = 42.75
BROKER_COMMISSION = 0.03

amount_paid = NUMBER_OF_SHARES * PURCHASE_PRICE
purchase_commission = amount_paid * BROKER_COMMISSION
amount_sold = NUMBER_OF_SHARES * SELL_PRICE
sell_commission = amount_sold * BROKER_COMMISSION
profit = amount_sold - amount_paid - purchase_commission - sell_commission

print(
    f'joe paid {amount_paid:,.2f} USD for 2000 shares\n'
    f'he also paid {purchase_commission:,.2f} USD commission to broker\n'
    f'the he sold them for {amount_sold:,.2f} USD\n'
    f'and paid {sell_commission:,.2f} USD commission\n'
    f'so the profit is {profit:,.2f} USD'
)

price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 10 / 100 * price
else:
    down_payment = 20 / 100 * price
print(f'Down payment is ${down_payment}.')

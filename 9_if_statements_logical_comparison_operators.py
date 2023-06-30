# if statements

price = 1000
has_good_credit = True
has_criminal_record = False

if has_good_credit:
    down_payment = 0.15 * price
elif not has_criminal_record:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'Down payment: {down_payment}')

# logical operators

if has_criminal_record and not has_criminal_record:
    print('Eligible for loan')

# comparison operators

temperature = 35

if temperature >= 30:
    print('It\'s a hot day')
else:
    print('It\'s not a hot day')


name = 'J'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name must be a maximum of 50 characters')
else:
    print('Name looks good')

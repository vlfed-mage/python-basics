for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(8):  # from 0 to 7
    print(item)

for item in range(5, 10):  # from 5 to 9
    print(item)

for item in range(5, 10, 2):  # from 5 to 9 with step 2
    print(item)

prices = [10, 20, 30]
total_price = 0
for el in prices:  # from 5 to 9 with step 2
    total_price += el

print(f'Total price: {total_price}')

# Nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')


# numbers = [5, 2, 5, 2, 2]
numbers = [2, 2, 2, 2, 5]
output = ''
for number in numbers:
    for x in range(number):
        output += 'x'
    output += '\n'
print(output)


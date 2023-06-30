# tuples

numbers = (1, 2, 3)  # tuples [кортежі] | immutable
# they only have two info methods: count and index

print(numbers[0])  # 1
# but
# numbers[0] = 10  # Tuples don't support item assignment | Error
# print(numbers)


# unpacking

coordinates = (1, 2, 3)

# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# res = x * y * z

# with unpacking it easier
# you can also use unpacking for lists as well

x, y, z = coordinates
res = x * y * z
print(x)  # 1
print(y)  # 2
print(z)  # 3
print(res)  # 6


# Dictionaries

# all keys should be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer['name'])  # John Smith
# print(customer['birth_date'])  # KeyError: 'birth_date'

# get() method

print(customer.get('name'))  # John Smith
print(customer.get('birth_date'))  # None
customer['birth_date'] = 'Jan 1 1980'
print(customer)  # {'name': 'John Smith', 'age': 30, 'is_verified': True, 'birth_date': 'Jan 1 1980'}

# Phone transformation

phone = input('Phone: ')
mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ''
for char in phone:
    output += f'{mapping.get(char)} '
print(output)

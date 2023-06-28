string = 'String'
# len()
print(len(string))

# upper()
print(string.upper())  # returns new modified string
print(string)

# lower()
print(string.lower())  # returns new modified string

# find()
print(string.find('S'))  # returns index of a char: 0
print(string.find('ing'))  # returns index of a char: 3 (because "ing" starts from index 3)

# replace()
print(string.replace('S', 's'))  # returns new modified string (replace exact value)
print(string.replace('ing', 'ong'))  # returns new modified string

# in
print('ing' in string)  # returns boolean: True
print('Ing' in string)  # returns boolean: False

birth_year = input('Birth year: ')
print(type(birth_year))

# age = 2023 - birth_year
# print(age)

# Traceback (most recent call last):
#   File "/home/valdo/development/python/hello-world/3_type_conversion.py", line 2, in <module>
#     age = 2023 - birth_year
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

age = 2023 - int(birth_year)
print(type(age))
# int()
# float()
# bool()
# str()

print(age)

# ----------------------

weight_in_pounds = input('Tell me your weight in pounds: ')
weight_in_kg = int(weight_in_pounds) * 0.45
print(weight_in_kg)

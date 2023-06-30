names = ['John', 'Bob', 'Vlad', 'Sarah', 'Mary']
print(names)

# the same as we got access to the characters in the string

print(names[0])  # the first character from the start:  "John"
print(names[-1])  # the last character from the end:  "Mary"
print(names[-2])  # the second character from the end:  "Sarah"
print(names[0:3])  # all characters from 0 index to 3rd:  ['John', 'Bob', 'Vlad']
print(names[0:])  # all characters from 0 index to the end:  ['John', 'Bob', 'Vlad', 'Sarah', 'Mary']
print(names[1:])  # all characters from 1 index to the end:  ['Bob', 'Vlad', 'Sarah', 'Mary']
print(names[:6])  # all characters from 0 index to 6th:  ['John', 'Bob', 'Vlad', 'Sarah', 'Mary']

# find the largest number in a list

numbers = [1, 2, 8, 9, 4, 7, 5]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)

# 2D Lists

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][2] = 30
print(matrix)  # [[1, 2, 30], [4, 5, 6], [7, 8, 9]]
print(matrix[0][2])  # 30

for row in matrix:
    for el in row:
        print(el)  # 1, 2, 30, 4, 5, 6, 7, 8, 9


# Lists methods

numbers = [5, 2, 7, 1, 4]
print(numbers)

# append()
numbers.append(20)
print(numbers)  # [5, 2, 7, 1, 4, 20]

# insert()
numbers.insert(0, 10)
print(numbers)  # [10, 5, 2, 7, 1, 4, 20]
numbers.insert(3, 8)
print(numbers)  # [10, 5, 2, 8, 7, 1, 4, 20]

# remove()
numbers.remove(2)
print(numbers)  # [10, 5, 8, 7, 1, 4, 20]

# pop()
numbers.pop()
print(numbers)  # [10, 5, 8, 7, 1, 4]

# index()
numbers.index(10)
print(numbers)  # 0
# numbers.index(2)
# print(numbers)  # ValueError: 2 is not in list

# in()
print(50 in numbers)  # False

# count()
numbers.insert(5, 8)
print(numbers)  # [10, 5, 8, 7, 1, 8, 4]
print(numbers.count(8))  # 2

# sort()
print(numbers.sort())  # None | sort() doesn't return any values
numbers.sort()
print(numbers)  # [1, 4, 5, 7, 8, 8, 10]

# reverse()
numbers.reverse()
print(numbers)  # [10, 8, 8, 7, 5, 4, 1]

# copy()
numbers2 = numbers
numbers.append(0)
print(numbers)  # [10, 8, 8, 7, 5, 4, 1, 0]
print(numbers2)  # [10, 8, 8, 7, 5, 4, 1, 0]
# but
numbers2 = numbers.copy()
numbers.append(110)
print(numbers)  # [10, 8, 8, 7, 5, 4, 1, 0, 110]
print(numbers2)  # [10, 8, 8, 7, 5, 4, 1, 0]

# clear()
numbers.clear()
print(numbers)  # []


# remove duplicates on list

numbers = [10, 5, 8, 7, 1, 8, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)  # [10, 5, 8, 7, 1, 4]

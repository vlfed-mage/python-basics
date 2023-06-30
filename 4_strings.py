course = 'Python course for beginners'
print(course)
course = "Python's course for beginners"
print(course)
course = 'Python\'s course for "beginners"'
print(course)

# multiple strings

letter = '''
Hi, John!

Here is our first email to you.

Thank you,
The support team

'''

print(letter)

# Indexing strings

course = 'Python\'s course for Beginners'
print(course[0])  # the first character from the start:  "P"
print(course[-1])  # the last character from the end:  "s"
print(course[-2])  # the second character from the end:  "r"
print(course[0:3])  # all characters from 0 index to 3rd:  "Pyt"
print(course[0:])  # all characters from 0 index to the end:  "Python's course for Beginners"
print(course[1:])  # all characters from 1 index to the end:  "ython's course for Beginners"
print(course[:5])  # all characters from 0 index to 5th:  "Pytho"
# and so on

name = 'Jennifer'
print(name[1:-1])

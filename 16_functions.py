def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user('John', 'Smith')  # positional arguments
print('//----')
greet_user(last_name='Miller', first_name='Kate')  # with keyword argument
# greet_user(last_name='Dou', 'John')  # Error. Positional argument after keyword argument
print('//----')
greet_user('John', last_name='Dou')  # keyword argument
# use it for improving of readability of your code. For example
print('//----')
print('Finish')


# return statement

def square(num):
    # return num * num
    print(num * num)  # 9


# by default functions in python return None, so
print(square(3))  # None


# emoji converter with functions

def emoji_converter(line):
    output = ''
    words = line.split(' ')
    emojis = {
        ':)': '😀️',
        ':(': '🙁️'
    }
    for word in words:
        output += f'{emojis.get(word, word)} '
    return output


message = input('> ')
print(emoji_converter(message))


# exceptions

# age = int(input('> '))
# # if you try to input text instead numbers, you'll get a ValueError
# print(age)  # asdf

# Traceback (most recent call last):
#   File "/home/valdo/development/python/python-basics/16_functions.py", line 49, in <module>
#     age = int(input('> '))
# ValueError: invalid literal for int() with base 10: 'asdf'

try:
    age = int(input('Age > '))
    income = 20000
    risk = income / age  # if age is 0, technically it's still number, but we'll get ZeroDivisionError
    print(age)
except ValueError:  # because this exception is only catching ValueError
    print('Invalid value')
# so we need to create another exception
except ZeroDivisionError:
    print('Age cannot be 0')

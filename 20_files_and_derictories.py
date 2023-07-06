# https://docs.python.org/3/library/pathlib.html#module-pathlib
from pathlib import Path

# Absolute path
# for windows   c:\Program Files\Microsoft
# for linux     /user/local/bin

# Relative path

path1 = Path()  # current directory
print(path1)

path2 = Path('ecommerce')  # ecommerce
print(path2)
print(path2.exists())  # True

path3 = Path('emails')  # check directory
print(path3.mkdir())  # create directory if it doesn't exist | returns None
# will be an error if directory or file already exists
# Traceback (most recent call last):
#   File "/home/valdo/development/python/python-basics/20_files_and_derictories.py", line 18, in <module>
#     path3.mkdir()
#   File "/usr/lib/python3.8/pathlib.py", line 1288, in mkdir
#     self._accessor.mkdir(self, mode)
# FileExistsError: [Errno 17] File exists: 'emails'

path4 = Path('emails')  # check directory
print(path4.rmdir())  # remove directory if exists | returns None


# we can also find all directories in a given path

p = Path()  # current directory
print(p.glob('*.*'))  # <generator object Path.glob at 0x7f2d0510f740>
for file in p.glob('*.*'):
    print(file)

# 11_while_loops.py
# 1_variables.py
# 20_files_and_derictories.py
# 19_generating_random_values.py
# 4_strings.py
# 6_string_methods.py
# .idea
# 3_type_conversion.py
# 10_weight_converter.py
# 2_receiving_input.py
# 9_if_statements_logical_comparison_operators.py
# 15_emoji_converter.py
# 13_lists.py
# 7_arithmetic_operations.py
# 16_functions.py
# 14_tuples_dictionaries_and_unpacking.py
# 5_formatted_strings.py
# .git
# 18_modules_and_packages.py
# 8_operator_precedence_and_math_functions.py
# 17_classes.py
# 12_for_loops.py

for file in p.glob('*'):  # all files and directories
    print(file)

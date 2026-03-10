#!/usr/bin/python3
"""Test all python-exceptions tasks"""
import sys
sys.path.insert(0, '.')

print("=" * 40)
print("TASK 0: Safe list printing")
print("=" * 40)
safe_print_list = __import__('0-safe_print_list').safe_print_list
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

print("\n" + "=" * 40)
print("TASK 1: Safe printing of integers")
print("=" * 40)
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer
value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

print("\n" + "=" * 40)
print("TASK 2: Print and count integers")
print("=" * 40)
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))
my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
try:
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
except IndexError as e:
    print("IndexError: {}".format(e))

print("\n" + "=" * 40)
print("TASK 3: Division with debug")
print("=" * 40)
safe_print_division = __import__('3-safe_print_division').safe_print_division
a, b = 12, 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
a, b = 12, 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

print("\n" + "=" * 40)
print("TASK 4: Divide a list")
print("=" * 40)
list_division = __import__('4-list_division').list_division
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
print("--")
my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("\n" + "=" * 40)
print("TASK 5: Raise exception")
print("=" * 40)
raise_exception = __import__('5-raise_exception').raise_exception
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

print("\n" + "=" * 40)
print("TASK 6: Raise a message")
print("=" * 40)
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

print("\n" + "=" * 40)
print("ALL TASKS COMPLETE!")
print("=" * 40)

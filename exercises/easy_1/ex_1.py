# pylint: disable-all
'''
Write a function that takes one integer argument and
returns True when the number's absolute value is odd, False otherwise.
'''
def is_abs_odd(integer):
    return abs(integer) % 2 != 0

print(is_abs_odd(3))
print(is_abs_odd(-3))
print(is_abs_odd(4))
print(is_abs_odd(-4))
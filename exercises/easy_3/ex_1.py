# pylint: disable-all
'''
Write a function that takes two arguments, a string and a positive integer,
then prints the string as many times as the integer indicates.
'''

def repeat(_str, _int):
    for _ in range(_int):
        print(_str)


repeat('Hello', 3)
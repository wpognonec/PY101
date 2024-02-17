# pylint: disable-all
'''
Write a function that returns the next to last word in the string argument.
Words are any sequence of non-blank characters.
You may assume that the input string will always contain at least two words.
'''

def penultimate(_str: str):
    str_list = _str.split()
    return str_list[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle(_str: str):
    str_list = _str.split()
    str_len = len(str_list)
    if not str_len:
        return "Your string is empty"
    elif str_len % 2 == 0:
        return f"{str_list[(str_len // 2) - 1]} {str_list[str_len // 2]}"
    return str_list[str_len // 2]

print(middle("") == "Your string is empty")
print(middle("Single") == "Single")
print(middle("Three words here") == "words")
print(middle("what is going on") == "is going")

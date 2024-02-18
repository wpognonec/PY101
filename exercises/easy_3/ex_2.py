# pylint: disable-all
import re
'''
Write a function that takes a string argument and returns
a new string that contains the value of the original string
with all consecutive duplicate characters collapsed into a single character.
'''

# def crunch(text: str):
#     crunched = ""
#     for char in text:
#         if not crunched.endswith(char):
#             crunched += char
#     return crunched

def crunch(text: str):
    crunched = re.sub(r"(.)\1+", r"\1", text)
    return crunched

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
'''
Write a function that takes a year as input and returns the century.
The return value should be a string that begins with the century number,
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000
comprise the 20th century.
'''
import math

def century(year):
    cent = math.ceil(year / 100)
    cent_str = str(cent)
    if cent % 100 in range (4,21):
        cent_str += "th"
    if cent % 10 == 1:
        cent_str += "st"
    if cent % 10 == 2:
        cent_str += "nd"
    if cent % 10 == 3:
        cent_str += "rd"
    return cent_str


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
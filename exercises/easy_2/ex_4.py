# pylint: disable-all

'''
Using the multiply function from the "Multiplying Two Numbers" exercise,
write a function that computes the square of its argument
(the square is the result of multiplying a number by itself).
'''

def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power(num, exp):
    total = 1
    for _ in range(exp):
        total = multiply(num, total)
    return total

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power(2,3) == 8)       # True
print(power(-8,3) == -512)   # True
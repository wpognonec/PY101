'''
Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
Bonus Question: Can you solve the problem by iterating over just the even numbers?
'''

for even in range(1,100):
    if even % 2 == 0:
        print(even)

for even in range(2,100,2):
    if even % 2 == 0:
        print(even)
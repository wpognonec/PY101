# pylint: disable-all

def oddities(_list: list):
    return _list[::2]

def evens(_list: list):
    return _list[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(evens([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evens([1, 2, 3, 4]) == [2, 4])        # True
print(evens(["abc", "def"]) == ['def'])     # True
print(evens([123]) == [])                # True
print(evens([]) == [])                      # True
# pylint: disable-all

def xor(val1, val2):
    return bool((val1 and not val2) or (val2 and not val1))


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
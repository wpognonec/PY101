# pylint: disable-all
'''
Write a program that asks the user to enter an integer greater than 0,
then asks whether the user wants to determine the sum or the product
of all numbers between 1 and the entered integer, inclusive.
'''

def get_num():
    while True:
        try:
            num = int(input("Please enter an integer greater than 0: "))
        except:
            continue
        if num > 0:
            return num

def get_choice():
    while True:
        choice = input("Enter 's' to compute the sum, or 'p' to compute the product: ").lower()
        if choice  == 's':
            return choice, "sum"
        elif choice == 'p':
            return choice, "product"

def compute(target, choice):
    if choice == "s":
        return sum(range(1,target+1))
    elif choice == "p":
        index = target
        total = 1
        while index > 1:
            if choice == 's':
                total += index
            else:
                total *= index
            index -= 1
        return total

def main():
    num = get_num()
    choice, choice_word = get_choice()
    total = compute(num, choice)
    print(f"The {choice_word} of the integers between 1 and {num} is {total}")
    
main()
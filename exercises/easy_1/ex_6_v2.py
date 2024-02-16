# pylint: disable-all
'''
Write a program that asks the user to enter an integer greater than 0,
then asks whether the user wants to determine the sum or the product
of all numbers between 1 and the entered integer, inclusive.
'''

def get_num():
    while True:
        try:
            nums_input = input("Please enter a list of integers greater than 0: ")
            nums_list = list(nums_input.split())
            nums = [int(n) for n in nums_list]
        except:
            continue
        return nums

def get_choice():
    while True:
        choice = input("Enter 's' to compute the sum, or 'p' to compute the product: ").lower()
        if choice  == 's':
            return choice, "sum"
        elif choice == 'p':
            return choice, "product"

def compute(num_list, choice):
    if choice == "s":
        return sum(num_list)
    elif choice == "p":
        total = 1
        for num in num_list:
            total *= num
        return total

def main():
    num_list = get_num()
    choice, choice_word = get_choice()
    total = compute(num_list, choice)
    print(f"The {choice_word} of the integers {num_list} is {total}")
    
main()
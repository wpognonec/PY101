# pylint: disable-all
'''
Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
The program must compute the tip, then print both the tip and the total amount of the bill.
You can ignore input validation and assume that the user will enter valid numbers.
'''

bill = float(input("Please enter the bill amount: "))
tip_rate = float(input("Please enter the tip percentage: "))
tip_amount = bill * tip_rate / 100
bill_total = bill + tip_amount

print(f"The tip is: ${tip_amount:.2f}")
print(f"The total is: ${bill_total:.2f}")

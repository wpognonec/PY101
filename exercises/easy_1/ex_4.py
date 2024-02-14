'''
Build a program that asks the user to enter the length and width of a room, in meters,
then prints the room's area in both square meters and square feet.
Note: 1 square meter == 10.7639 square feet
'''
choice = None
while choice not in ["m", "f"]:
    choice = input("Are you using meters or feet (m/f?")
match choice:
    case "m":
        units = "meters"
    case "f":
        units = "feet"

length = float(input("Length in meters: "))
width = float(input("Width in meters: "))

print(f"Area in square meters is: {(length * width):.2f}")
print(f"Area in square feet is: {(length * width * 10.7639):.2f}")
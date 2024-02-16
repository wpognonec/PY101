# pylint: disable-all
'''
Build a program that asks the user to enter the length and width of a room, in meters,
then prints the room's area in both square meters and square feet.
Note: 1 square meter == 10.7639 square feet
'''
choice = None
while choice not in ["m", "f"]:
    choice = input("Are you using meters or feet (m/f)?")
match choice:
    case "m":
        unit1 = "meters"
        unit2 = "feet"
    case "f":
        unit1 = "feet"
        unit2 = "meters"

length = float(input(f"Length in {unit1}: "))
width = float(input(f"Width in {unit1}: "))
area = length * width
unit_mod = 10.7639 if unit1 == "meters" else (1 / 10.7639)

print(f"Area in square {unit1} is: {area:.2f} ({area * unit_mod:.2f} square {unit2})")

# pylint: disable-all
import datetime

age = int(input("What is your age? "))
retire_age = int(input("What age would you like to retire at? "))
current_year = datetime.date.today().year
print(f"It's currently {current_year}. You will retire in {current_year + retire_age - age}")
print(f"You only have {retire_age - age} to go!")
# pylint: disable-all
import random

name = input("Please enter your name: ")
age = random.randint(20,100)
print(f"{name if name != "" else "Teddy"} is {age}")
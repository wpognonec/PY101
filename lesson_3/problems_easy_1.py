# Question 1
# numbers = [1, 2, 3]
# numbers[6] = 5 # Raises index out of range error

# # Question 2
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False
# print(str1[len(str1)-1] == "!")
# print(str1.endswith("!"))
# print(str2[len(str2)-1] == "!")
# print(str2.endswith("!"))

# # Question 3
# famous_words = "seven years ago..."
# print(f"Four score and {famous_words}")
# print("Four score and " + famous_words)

# # Question 4
# munsters_description = "the Munsters are CREEPY and Spooky."
# print(munsters_description.capitalize())
# # => 'The munsters are creepy and spooky.'

# # Question 5
# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

# # Question 6
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."
# print("Dino" in str1)
# print("Dino" in str2)

# # Question 7
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append(("Dino"))
# print(flintstones)

# # Question 8
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(["Dino", "Hoppy"])
# print(flintstones)

# # Question 9
# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected return value:
# # => 'Few things in life are as important as '
# print(advice[:advice.index("house")])
# print(advice.split("house")[0])

# # Question 10
# advice = "Few things in life are as important as house training your pet dinosaur."
# print(advice.replace("important", "urgent"))
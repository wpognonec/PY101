# # Question 1
# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first())
# print(second())

# #The results are different as first() is returning a dictionary
# # while second() is returning None and the dictionary is on the line below.

# # Question 2
# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list) # [1,2]
# print(dictionary) # {'first': [1,2]}

# # Question 3
# # A
# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")         # "one is: ["one"]"
# print(f"two is: {two}")         # "two is: ["two"]"
# print(f"three is: {three}")     # "three is: ["three"]"

# # B
# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")         # "one is: ["one"]"
# print(f"two is: {two}")         # "two is: ["two"]"
# print(f"three is: {three}")     # "three is: ["three"]"

# # C
# def mess_with_vars(one, two, three):
#     one[0] = "two"
#     two[0] = "three"
#     three[0] = "one"

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}")         # "one is: ["two"]"
# print(f"two is: {two}")         # "two is: ["three"]"
# print(f"three is: {three}")     # "three is: ["one"]"

# # Question 4

# def is_an_ip_number(word):
#     return int(word) in range(256)

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False

#     return True

# print(is_dot_separated_ip_address("1.1.1.1"))
# print(is_dot_separated_ip_address("1.1.1"))
# print(is_dot_separated_ip_address("1.1.1.300"))
# print(is_dot_separated_ip_address("1.1.1.1.1"))

# # Question 5
# if False: # This evaluates as False, so greeting does not get initialized.
#     greeting = "hello world"

# print(greeting) # This will raise a variable not found error
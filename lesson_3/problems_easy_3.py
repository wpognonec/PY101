# # Question 1
# numbers = [1, 2, 3, 4]

# # while numbers:
# #     numbers.pop()

# # while numbers:
# #     del numbers[0]

# # numbers = []

# numbers.clear()

# print(numbers)

# # Question 2
# print([1, 2, 3] + [4, 5]) #[1,2,3,4,5]

# # Question 3
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1) # "hello there"

# # Question 4
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1) #[{"first": 42}, {"second": "value2"}, 3, 4, 5]

# # Question 5
# # def is_color_valid(color):
# #     if color == "blue" or color == "green":
# #         return True
# #     else:
# #         return False

# # def is_color_valid(color):
# #     return (color == "blue" or color == "green")

# def is_color_valid(color):
#     return (color in ["blue", "green"])
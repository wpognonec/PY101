# import math
# # Question 1
# for i in range(10):
#     print(f'{" " * i}The Flintstones Rock!')

# # Question 2
# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0: # Purpose is to determine if number is divisible by divisor
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# print(factors(-4))

# # Question 3
# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer
# # This method mutates the original buffer and returns a shallow copy

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer
# # This method does not mutate the buffer passed into the function
# # A shadow copy buffer is assigned the value of the argument + new element, creating a new list
# # The new list is then returned leaving the original copy unchanged

# # Question 4
# print(0.3 + 0.6) #0.89999...
# print(0.3 + 0.6 == 0.9) # False due to floating point precision

# # Question 5
# nan_value = float("nan")
# print(math.isnan(nan_value))

# # Question 6
# answer = 42

# def mess_with_it(some_number):
#     return some_number + 8

# new_answer = mess_with_it(answer)
# print(answer - 8) # 34

# # Question 7
# munsters = {
#     "Herman": {"age": 32, "gender": "male"},
#     "Lily": {"age": 30, "gender": "female"},
#     "Grandpa": {"age": 402, "gender": "male"},
#     "Eddie": {"age": 10, "gender": "male"},
#     "Marilyn": {"age": 23, "gender": "female"},
# }

# def mess_with_demographics(demo_dict):
#     for key, value in demo_dict.items():
#         value["age"] += 42
#         value["gender"] = "other"

# mess_with_demographics(munsters)
# print(munsters)
# # Yes the data gets modified as the value variable in the for loop is an reference pointing to a mutable dict object.
# # Using the value[key] += is a mutating function

# # Question 8
# def rps(fist1, fist2):
#     if fist1 == "rock":
#         return "paper" if fist2 == "paper" else "rock"
#     elif fist1 == "paper":
#         return "scissors" if fist2 == "scissors" else "paper"
#     else:
#         return "rock" if fist2 == "rock" else "scissors"
    
# print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock")) # paper

# # Question 9
# def foo(param="no"):
#     return "yes"

# def bar(param="no"):
#     return param == "no" and foo() or "no"

# print(bar(foo())) # "no"

# # Question 10
# a = 42
# b = 42
# c = a

# print(id(a) == id(b) == id(c)) # True
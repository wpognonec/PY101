'''
Write a function that determines the mean (average) of the three scores
passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

    90 <= score <= 100: 'A'
    80 <= score < 90: 'B'
    70 <= score < 80: 'C'
    60 <= score < 70: 'D'
    0 <= score < 60: 'F'

Tested values are all between 0 and 100. There is no need to check for
negative values or values greater than 100.
'''

def get_grade(grade1, grade2, grade3):
    mean = (grade1 + grade2 + grade3) // 3

    if mean in range(90, 101):
        return "A"
    if mean in range(80, 90):
        return "B"
    if mean in range(70, 80):
        return "C"
    if mean in range(60, 70):
        return "D"
    return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
from icecream import ic

# Variables
name = "Chakri"
age = 20
course = "Python"

# Print variables
ic(name)
ic(age)
ic(course)

# Print expressions
x = 10
y = 5

ic(x + y)
ic(x * y)

# Function Example
def square(num):
    ic(num)
    return num * num

result = square(8)

ic(result)
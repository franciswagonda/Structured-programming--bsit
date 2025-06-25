# def sum_of_numbers(a,b):
#     return a + b
# print((sum_of_numbers(90,80)))

# def square_of_number(x):
#     return x * x    
# print(square_of_number(9))

# def multiply_numbers(a, b):
#     return a * b
# print(multiply_numbers(6, 7))

# def divide_numbers(a, b):
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a / b    
# print(divide_numbers(700,9))

"""
a function is a block of code of that contains specific topic for our program

def name (parameter1, parameter2......):
    logic

types of functions:
   1. built- in - functions
   2. User defined functions
   3. anonymous functions
   4. Recursive functions
   5. Higher Orer functiions
   6. Pure functions
   7. Impure functions
   8. callback function
   9. method functions
   10. Generator functions

"""

"""
 2. User defined functions

a) returning functions
b) void functions
"""

""""
a) Returning functions


#structure
def name (parameter1, parameter2......):
    logic
    return value
............
"""
def addition(number_one ,number_two):
    sum = number_one + number_two
    return sum

print(addition(5,9))


""""
b) void function

#structure

def name (parameter1, parameter2......):
    logic
"""
def addition(number_one ,number_two):
    sum = number_one + number_two
    print(sum)

addition(67,9)

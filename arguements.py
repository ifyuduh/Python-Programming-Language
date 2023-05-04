# Positional arguments:
# Positional arguments are the most common type of arguments used in Python.
# These arguments are passed to a function in a specific order, and the order of the arguments
# must match the order of the parameters in the function definition. For example:

def add_numbers(x, y):
    return x + y

result = add_numbers(2, 3)
print(result) # Output: 5

'''
In this case, the value 2 is passed as the first argument, which corresponds to the x parameter
in the function definition,
and the value 3 is passed as the second argument, 
which corresponds to the y parameter in the function definition.

'''

# Keyword Argument:
# keyword arguments, you explicitly specify which parameter 
# each value corresponds to by using the parameter name as a keyword. For example, 
# using the same add_numbers function, you could pass the numbers as keyword arguments like this:

result = add_numbers(x=2, y=3)

# value of the x parameter is 2, and the value 3 is passed as the value of the y parameter.
# The main difference between positional and keyword arguments is
# that with positional arguments, the order of the values matters, while with keyword 
# arguments, the order does not matter as long as you use the correct parameter name

# Default arguments:
# Default arguments are used to specify a default value for a parameter in a function definition. 
# If a value is not provided
# for that parameter when the function is called, the default value is used instead. For example

def multiply_numbers(x, y=2):
    return x * y

result1 = multiply_numbers(3) # y defaults to 2
result2 = multiply_numbers(3, 4) # y is explicitly set to 4
print(result1) # Output: 6
print(result2) # Output: 12

# Variable-length arguments:
# Variable-length arguments allow a function to accept
# any number of arguments. In Python, variable-length arguments are denoted by an asterisk (*)
# before the parameter name. There are two types of variable-length arguments in Python: 
# *args and **kwargs. For example:

def concatenate_strings(*args):
    return " ".join(args)

result = concatenate_strings("Hello", "world", "!")
print(result) # Output: "Hello world !"

#Example of ***kwargs

def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_student_details(name="John", age=20, major="Computer Science")

# In this example, the print_student_info function accepts a 
# required name parameter, followed by **kwargs, which allows the function
# to accept any number of additional keyword arguments.

# When calling the function, you can pass any number of
# keyword arguments as you like, which will be collected
# into a dictionary with the parameter name as the key and the argument value as the value.

# In this example, we're passing three keyword arguments, 
# age, major, and gpa, each with a different value.
# The function then prints out the student's name, followed by each of the additional keyword 
# arguments and their values.


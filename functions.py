# PYTHON FUNCTIONS
# What is a python function?
# python functions perform a specific task or return a value
# In Python, a function is a block of code that performs a specific task or
# returns a value. When you call a function in Python, you are asking the program
# to execute that block of code and perform the task or 
# calculation that the function is designed to do.
# # everyday life, we use "functions" all the time without even realizing it. For example,
# when you turn on a lamp,
# you are using a "function" that is built into the lamp.
# When you press a button on a remote control, you are using a "function" that is built into the remote
# control.

# In programming, a function is basically a way of organizing code so that it can be reused over 
# and over again. It's like a mini-program that you can call whenever you need to do a specific task. 
# For example, you might create a function that adds two numbers together, or a function that sorts a 
# list of items in alphabetical order.

# One of the biggest benefits of using functions is that they allow you to write code that is
# easier to read and understand. Instead of having a huge block of code that does everything all at
# once, you can break it up into smaller pieces that each do one thing really well. This makes it much
# easier to make changes to your code later on, because you only need to change one function instead of
# the entire block of code.

# So in a nutshell, a function is a way of organizing code so that it can be reused over and over again,
# and it makes your code easier to read and understand.

# # why the def before a function?

# Great question! In Python, def is a keyword that is used to define a function.
# The word "def" is short for "define", which means to create or establish something.
# So when you write a function in Python, you start with the def keyword, 
# followed by the name of the function, and then any parameters the function 
# might take in between parentheses. After that, you write the body of the function, 
# which is the code that will be executed when the function is called. 

#Types of functions
# - Create your own function

# - Modules

# - Built in function

# Built-in Functions: Python provides a set of built-in functions that are readily available for use. 
# These functions perform common tasks, such as converting data types, manipulating strings,
# and performing mathematical operations.

# print() function: The print() function is a built-in function that prints the specified value 
# or variable to the console or output device.

print("Jobina is blessed")

# len() function: The len() function is used to return the length of a string, list, tuple, or other iterable object.
# declare a string variable

my_string = "Hello, world"
string_length = len(my_string)
print("The number of strings is:", string_length )
 
# type() function: The type() function is used to return the data type of a variable or expression.
my_string = "Hello, World!"
my_number = 42
my_list = ["apple", "banana", "cherry"]
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Use the type() function to get the data type of each variable
print("The data type of my_string is:", type(my_string))
print("The data type of my_number is:", type(my_number))
print("The data type of my_list is:", type(my_list))
print("The data type of my_dict is:", type(my_dict))

# input() function: The input() function is used to accept user input from the console or input device.
# Prompt the user to enter their name
name = input("What is your name? ")

# Greet the user with their name
print("Hello,", name, "nice to meet you!")

# range() function: The range() function is used to generate a sequence of numbers, 
# which is often used in for loops to iterate over a specific range of values.

# Use the range() function to generate a sequence of numbers
for i in range(5):
    print(i)

# In this example, we use the range() function to generate a sequence of numbers from 0 to 4
# (5 is not included). We then use a for loop to iterate over this sequence 
# and print each number to the console using the print() function.

# The range() function can also be used to generate sequences of numbers with
# different starting points, increments, and lengths.

# 1. starting points and lengths
# Generate a sequence of numbers starting from 5 and ending at 9
for i in range(5, 10):
    print(i)

# In this example, the range() function is used to generate a sequence of numbers starting from 5 and
# ending at 9 (10 is not included). 

#2. Starting points, lengths and increments
# # Generate a sequence of even numbers between 0 and 10
for i in range(0, 11, 2):
    print(i)
    
# In this example, the range() function is used to generate a sequence of even numbers between 0 and 10,
# with an increment of 2.

#3. Reverse order
# Generate a sequence of numbers in reverse order

for i in range(10, 0, -1):
    print(i)
    
# In this example, the range() function is used to generate a sequence of numbers in reverse order, 
# starting from 10 and ending at 1. 
# In this code snippet, the range() function is used to generate a sequence of numbers from 
# 5 to 1 (in reverse order). The third argument in the range() function is -1, which specifies
# that the sequence should be generated in reverse order, decreasing by 1 at each step.
# The reason why we use -1 here is because the third argument specifies the step value, 
# or the amount by which the sequence should be incremented or decremented at each step.

# In this case, we want to generate a sequence that counts down from 5 to 1 in reverse order, 
# so we need to decrement the sequence by 1 at each step. The range() function uses the third 
# argument to determine the step value, which is why we use -1 here to specify that we want the 
# sequence to be generated in reverse order.

# Note that the range() function in Python generates sequences that are half-open,
# meaning that the stop value (in this case, 0) is not included in the sequence. 
# So if we wanted to generate a sequence from 5 to 1 (inclusive), we would need to change 
# the second argument in the range() function to 6, like this:

def calculate_sum(x,y):
    sum=x+y
    return sum

result=calculate_sum(60,10)
#print(result)
print("The sum of 5 and 7 is:", result )

#In this example, we define a function called calculate_sum that takes two parameters x and y and
# returns their sum. We then call the function with the values 5 and 7 and store the result in a 
# variable called result. 
#Finally, we print out a message that includes the value of result.


# simple print statement
# print function
print("Hello future programmer")

def say_hello(name):
    print("hello, "+ name +"!")
    
#This function is called say_hello and it takes one parameter called name. 
# The function will print out a personalized greeting that includes the name passed to the function.
#To use this function, you would call it like this
    
say_hello('Jobina')

# Task: 
# Write a function called calculate_area() that takes two parameters, width and height, and calculates the area of a rectangle using the formula area = width * height. The function should return the area as a result.

# Hints:
# The parameters width and height should be numbers (float or integer).
# The result should also be a number (float or integer).



def calculate_area(width, height):
    area=width * height
    print(area)


height=10
width=5
result=calculate_area(width, height)

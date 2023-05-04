#Types of Strings:
#Strings can be represented by
STR1 = "double quotes"
STR2 = 'single quotes'
STR3 = '''Three single quotes'''
STR4 = """ Double quotes as strings"""

# Numbers:
Num = 24 #integer
Num = 6.7 #float

#List: 
# This is a Collection of variables. It is also called an array in other programming languages.
# List can contain multiple data types. A float, integer or string can be in a list.
# Lists are enclosed in square brackets.
# All elements in a list must be  separated by a comma spacing is not mandatory
# List is mutable

my_first_list = [STR4, 12, 7.8, "Tech is good"]

print(my_first_list)

# Tuple:
# Collection of multiple data types but it is enclosed in () bracket
# Tuples are immutable

my_first_tuple = (STR4, 12, 7.8, "Tech is good")

print(my_first_tuple)

#Dictionary:
# This is a collection of key value pairs
# All elements are usually in pair Key:value
# curly brackets{}

my_first_dictionary = {"DevOps" : "Collaboration", "Certification" : "gain hands on experience", "Experience" : [4,6,8,] }
print(my_first_dictionary)

print(type(my_first_tuple))
print(type(my_first_dictionary))
print(type(my_first_list))

# Boolean
x = True
y = False
print(type(x))




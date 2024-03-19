name = "Jobina"
profession = " Devops Eng"

print("My name is ", name)#regular print function
print("My name is  {}" .format(name)) # diff way of printing single string
print("My name is {} and i am a {}".format(name, profession)) #printing multiple strings
print(f"My name is {name} and i am a {profession}") #Using the f string


# Concatenation
#Concatenation in Python refers to the process of combining two or more strings
# together to create a single string. 
#This operation is commonly performed using the + operator or the += operator

str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2
print(result) # Output: Hello, World


#You can also use the += operator to concatenate strings and assign the result back to a variable:

str1 = "Hello"
str2 = "World"
str1 += ", " + str2
print(str1) # output: Hello, World

#Additionally, you can use the join() method to concatenate multiple strings from a list:
strings = ["Hello", "World"]
result = ", ".join(strings)
print(result) # Output: Hello, World 




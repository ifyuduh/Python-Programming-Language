#There are so many built in functions.
# This is an example of capitalize function
message=("i hope you have a good life")
print(message)
print(message.capitalize())
Message=message.capitalize()
print(Message)

"""

#dir() function
print(dir(message)) #This prints as a list all the built in functions available to message
print(dir([]))
print(dir(""))
print(dir({}))
print(dir(()))


print(message.upper())
print(message.islower()) #This returns a boolean value true or false

print(message.find("life"))
print(message)
print(message[23:28]) #Slicing
print(message.find("not")) #string not in the sentence



seq1=("20", "40","70", "70")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

"""

# Lists are mutable. How to change list with append function.
""""
Designers=["Zara", "Givenchy", "Gucci", "Fendi", "Primark"]
print(Designers)
Designers.append("Zizi Cadow")
print(Designers)
Designers.extend(["Jojo","Devops","Class"]) #to extend the list
print(Designers)
Designers.insert(2,"Giovanni") # This inserts in the third place the string Giovanni
print(Designers)
Designers.pop()
print(Designers) #pop removes/deletes the last word

"""

# Tuples are immutable


# Dictionary change with built in functions
Names = {"name":"Jobina", "Job":"Devops Eng", "Kids":"Two" }
print(Names.keys())  #prints key 
print(Names.values()) #Prints values
Names.clear() #Clears the tuple
print(Names)

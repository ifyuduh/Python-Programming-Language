""""
In computer programming, a loop is a way to repeat a set of instructions 
multiple times. It's like a machine that keeps doing the same task until 
it's told to stop.
There are two main types of loops in the Python programming language:

for loop: This type of loop is used to go through a list of things,
like a shopping list or a list of names. Each time the loop runs, it takes one
item from the list and does something with it. For example, if you had a list of 
animals, you could use a for loop to print out each animal's name one by one.

while loop: This type of loop is used to repeat a set of 
instructions as long as a certain condition is true. 
For example, you could use a while loop to keep counting up 
until you reach a certain number. The loop would keep running 
until the number you're counting gets to the stopping point.

"""

# FOR LOOP

Jobina = "DevOps Engineer"
for i in Jobina:
    print(f" The value of i is now", i )
    


Vaccines = ("pfizer", "Moderna", "Covaxin", "Astrazeneca") #iterating over a tuple

for vac in Vaccines: #this can be any variable it can be i, vac or anything
  print(f"{vac}  vaccines provides immunization against Covid 19")
    
    
Vaccines = ["pfizer", "Moderna", "Covaxin", "Astrazeneca"] #iterating over a list
for i in Vaccines:
  print(f"{i} is one of the best Vaccines")


#WHILE LOOP
x = 0
while x <= 10:
    print("value of x is:", x) #This is an infinite loop
    x+=1 #stops the loop
    
    




    
    
    

# Arithmetic Operators +, -, *,/,

x = 16 #+
y = 8
total =(x + y)
print(total)

total = (y - x) #-
print(total)

total = (x * y) #*
print(total)

total =(x/8) # / division
print(total)

total = y % x
print(total) # This prints the remainder

total = y**x
print(total) #raise to the power

# Comparison Operators
# it returns a boolean value true or false

a = 30
b = 60
result = (a > b)
print(result)

a = 30
b = 60
result = (a < b)
print(result)

a = 30
b = 60
result = (a == b)
print(result)

a = 30
b = 60
result = (a != b)
print(result)

a = 30
b = 60
result = (a >= b)
print(result)

a = 30
b = 60
result = (a <= b)
print(result)

# Assignment Operators

c = 0
d = 1
c+=d #c =c+d
print(c)

c = 0
d = 1
c-=d #c =c-d this also applies for divide and multiplication
print(c)

#Logical operators 
# And, or

x = 30
y = 40

j = 90
k = 100
output = (y > x) or (k > y) #if any of the options are true, it will return as true. 
print(output) # if both options are false then, it will return false.

output = (x > y) and (k > j) # if one option is false, then it will return false
print(output)  #to get true, the both operands have to be true

#negate with not
output = not(y > x )
print(output)

# Membership Operator "in" "not in"

my_new_list = ["Jojo", 34, 5.6, "Tomatoes"]
output = "Jojo" in my_new_list
print(output)

my_new_list = ["Jojo", 34, 5.6, "Tomatoes"]
output = "Jojo"  not in my_new_list
print(output)

# Identity Operators
a = 12
b = 15

result = a is b
print(result)

result = a is not b 
print(result)
















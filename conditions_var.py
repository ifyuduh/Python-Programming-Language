"""
Testing our knowledge on conditions 
and different data types. 

"""
print("This IT organization has people with different skill sets.")
print("We need a Devops Engineer")
print("Find your match:")
print("Please enter capitalized values")


Devops = ["Jenkins", "Ansible","Bash", "Python", "Puppet" ] #list
Devs = ("Nodejs", "Angular JS.", "Java", ".net", "python" ) #tuple
contract_emp1 = {"Name" : "Joseph", "Skill" : "Blockchain", "Employee code" : "2023"} #dictionary
contract_emp2 = {"Name" : "Cynthia", "Skill" : "AI", "Employee code" : "2022"}

user_skill = input("Enter your desired skill: ") #Using the input function.
#print(user_skill)

# Check in the database if we have this skill.
if user_skill in Devops:#using the membership operator
   print(f"we have {user_skill} in DevOps team. ")
elif user_skill in Devs:
   print(f"we have {user_skill} in Devs team. ")
elif (user_skill in contract_emp1.values()) or (user_skill in contract_emp2.values()):
   print(f"We have contract employee {user_skill}  ")
else:
   print("skill not found")
   print("Please Capitalise your values")

#here we are checking the values. Skill is the key but we are going to use some functions to check the values
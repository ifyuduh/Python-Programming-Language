"""
Testing our knowledge on conditions 
and different data types. 

"""
print("This IT organization has people with different skill sets.")
print("We need a Devops Engineer.")

print("Find our match: ")

Devops_skill = ["Jenkins", "Ansible","Bash", "Python", "Puppet" ] #list
Devs_skill = ("Nodejs", "Angular JS.", "Java", ".net", "python" ) #tuple
contract_emp = {"Name" : "Joseph", "Skill" : "Blockchain", "Employee code" : "2023"} #dictionary
contract_emp = {"Name" : "Cynthia", "Skill" : "AI", "Employee code" : "2022"}

user_skill = input("Enter your desired skill ") #Using the input function.
#print(user_skill)

# Check in the database if we have this skill.
if user_skill in Devops_skill:#using the membership operator
   print(f"You are a Devops Eng:Therefore you are a match.")

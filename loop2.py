"""
# Nested loops
Vaccines = ["pfizer", "Moderna", "Covaxin", "Astrazeneca"] 
for vac in Vaccines:
    print("")
    print("I would like a shot of," )
    for i in vac:
        print(i)
"""        
import time  
x = 2
while True:
    print("value of x is:", x)
    print("looping")
    x*=2
    time.sleep(1)  
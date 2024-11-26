# While Loop
a = 2
while a < 6:
    print (a)
    a += 1

# Break statement 
a =1 
while a < 11:
    print (5,"X",a,"=",a*5)
    if a == 6 :
        break
    a += 1
    
# Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # continue statement
    print (i)

# For Loop
mybasket = ["Grapes", "banana", "cherry"]
for x in mybasket:
    print(x)
    
# Nested Loops
course = ["Car", "Motorcycle", "Bicycle"]
student = ["John", "Shelly", "Mike"]
for x in course:
    for y in student:
        print(x, y)
        
# Pattern Work
for i in range(1,6):
    print(i*"*")
    
 
    

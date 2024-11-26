print("Hello")
print('hello')

# declaring a vairable  
# print after declaring a variable
age = 29
age
print("The age is : " ,age)

# casting to find the data type
print(type(age))

# indentation use
if(age>20):
 print(age)
 
# Mulitple variable and multiple values
 x,y,z ="Roughe","Noir","Blanc"
 print(z)
 
 # Mulitple variable and single values
 x=y=z= "Primordial" 
 print(z)
 
 name = "Kushal"
 print(name)
 name ='Rohit'
 print(name)
 
 #Case sensitive-
 age = 5
 AGE = 10
 print(age)
 print(AGE)
 
 # _ unserscore can be use in a variable declaration
my_school="Riya"
print(my_school)
_my_name="Riya"
print(_my_name)

# Upper case and lower case
age=5
AGE=20
print(age)

# Camel Case
mySchoolName= "Mike"
print(mySchoolName)

#Pascal Case
MySchoolName="Mike"
print(MySchoolName)

# Snake Case
My_School_Name = "Mike"
print(My_School_Name)

# Concatenation 
green ="Vert"
yellow = "Jaune"
blue = "Bleu"
print(green,yellow,blue)

# using + oprrator
print(green + yellow + blue)

# + operator will not work on different datatypes
#a = 5
#b = "year"
#print(a+b)

# global varibales outside the function

a= 35

def myclass():
    print("My age is" ,a)
myclass()

# global variables inside a function
def myclass():
   
    global a
    a = "Examination"
myclass()

print("I am studying for" ,a)

# Data types

#we are using

a="Python is good"        #Text type -str
ax ='Python is similiar to R Programing'
print(ax)
a=10
print(a)
b = 35.8            # Numeric types int, float,complex
print(b)
a = 3+3j   
print(a)

# Random number
import random
print(random.randrange(20,30))

# Multi line string
quote = '''All suffering 
    in the world 
        is born from 
            an individual’s 
                incompetence'''
print(quote) 

# Python - Slicing Strings
b = "Eternal Abyss!"
print(b[1:4])

# Slice From the Start
b = "Hello, World!"
print(b[1:3])
#Slice To the End
b = "Infinity"
print(b[3:])
#Negative Indexing
b = "Eternity"
print(b[-4:-2])

# Python - Modify Strings
#Upper Case
a = "nightmare castel!"
print(a.upper())
#Lower Case
a = "FROZEN HELL COCYTUS!"
print(a.lower())

#Python - Escape Characters

txt = 'It\'s alright.'
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 

# Python Booleans  expression is True or False.
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Python Operators

#Arithmetic operators   (+,-,*,&,%)
x = 8
y = 7
print("Division Operator (x/y): " , x / y)
print("Multiplication Operator (x*y): " , x * y)
print("Addition Operator (x+y): " , x + y)
print("Subtraction Operator (x-y): " , x - y)

#Assignment operators
x = 5
x -= 3        # x = x-3   .i.e x=5-3=2
print(x)

x*=3
print(x)    # 6

x/=2
print(x)

#Comparison operators
x = 5
y = 3
print(x == y)
print(x!=y)
print(x<=y)

#Logical operators
x = 5
#print(x > 3 and x < 10)
print(x > 3 or x > 10) 

def call_by_value(x):
    x = x * 2
    print("in function value updated to", x)
    return

b = 110 ;
call_by_value(b)
print(b)

var1 = "big"
var2 = "data"
print(var1, var2)




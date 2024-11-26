# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Oct 15 14:15:28 2024)---
pip install pandas
restart
runfile('C:/Users/marmi/.spyder-py3/temp.py', wdir='C:/Users/marmi/.spyder-py3')
runfile('C:/Users/marmi/.spyder-py3/pythonscript.py', wdir='C:/Users/marmi/.spyder-py3')
runcell(0, 'C:/Users/marmi/.spyder-py3/pythonscript.py')
runfile('C:/Users/marmi/.spyder-py3/pythonscript.py', wdir='C:/Users/marmi/.spyder-py3')
runcell(0, 'C:/Users/marmi/.spyder-py3/pythonscript.py')
runfile('C:/Users/marmi/.spyder-py3/pythonscript.py', wdir='C:/Users/marmi/.spyder-py3')
runfile('C:/Users/marmi/.spyder-py3/List Script.py', wdir='C:/Users/marmi/.spyder-py3')
runfile('C:/Users/marmi/.spyder-py3/Tuple Script.py', wdir='C:/Users/marmi/.spyder-py3')
var1 = "big"
var2 = "data"
print(var1, var2)

var1 = "big"
var2 = "data"
print(var1+var2)
runfile('C:/Users/marmi/.spyder-py3/List Script.py', wdir='C:/Users/marmi/.spyder-py3')
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.pop(4)
mylist.pop()  # if index not defined it will delete the last element
print(mylist)

course = ["BBA", "BCA", "MCA","B.Com"]
print(course)
runfile('C:/Users/marmi/.spyder-py3/List Script.py', wdir='C:/Users/marmi/.spyder-py3')

course = ["BBA", "BCA", "MCA","B.Com"]
print(course)
course. clear ()
print(course)
runfile('C:/Users/marmi/.spyder-py3/List Script.py', wdir='C:/Users/marmi/.spyder-py3')

course = ["BBA", "BCA", "MCA","B.Com"]
for x in course:
    print(x)
runcell(0, 'C:/Users/marmi/.spyder-py3/Tuple Script.py')
runfile('C:/Users/marmi/.spyder-py3/Tuple Script.py', wdir='C:/Users/marmi/.spyder-py3')

a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
b = b.extend(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)
a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
b.extend(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)
a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
b.append(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)

fruits = ("apple", "banana", "cherry") # Packing process
(green, yellow, red) = fruits # unpacking
print (green)
print (yellow)
print (red)

t1 = ("Justice","Covenant","Hope","Charity","Patience","Purity","Wisdom")
t2 = ("Judgement","Heaven","Dominion","Trials","Salvation","Glory","Rigor")
t3 = t1+t2
print(t3)
a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
b.extend(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)
a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
b[2]= "Rouge"
#b.extend(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)

set1 = {"Wrath","Pride","Gluttony","Lust","Envy","Sloth","Greed"}
set2 = {"Death","Poison","Temptation","Annihilation"}
set1.update(set2)
print(set1)
runfile('C:/Users/marmi/.spyder-py3/Set Script.py', wdir='C:/Users/marmi/.spyder-py3')
mycourse = ("BCA", "BBA", "MBA", "MCA", "MTech")
(amit, sumit,*vaibhav, tarun) = mycourse
print(amit)
print(sumit)
print(*vaibhav)
print(tarun)
mycourse = ("BCA", "BBA", "MBA", "MCA", "MTech")
(amit, sumit,vaibhav,*tarun) = mycourse
print(amit)
print(sumit)
print(vaibhav)
print(*tarun)
print(vaibhav)
s= {"school","class","Exam","Result"}
print(s)
s.clear()
print(s)
s.clear()
print(s)
 Update Method
set1 = {"PDGBA", "PGDAC”,"PGDIT"}
set2 = {'Amit', "Tarun", "Mohit"}
set2 = set1.update (set2) # update ( ) method
print (set1)

set1 = {"PDGBA", "PGDAC" , "PGDIT", "CDAC"}
set2 = {'Amit', "Tarun", "Mohit", "CDAC"}
set3 = set1.union (set2) # union () method
print (set3)
mydict = {
"brand": "Nokia", # key value pair
"model": "premium",
"year": 2010
}
print(mydict)
set1 = {"PDGBA", "PGDAC" , "PGDIT", "CDAC"}
set2 = {'Amit', "Tarun", "Mohit", "CDAC"}
set3 = set1.union (set2) # union () method
print (set3)

set1 = {"PDGBA", "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ," Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)
 Update Method     It will add the elements of one set in another
set1 = {"PDGBA", "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ," Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)

set1 = {"PDGBA", "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ," Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1
runfile('C:/Users/marmi/.spyder-py3/Set Script.py', wdir='C:/Users/marmi/.spyder-py3')

set1 = {"PDGBA", "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ," Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)

set1 = {'PDGBA', "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ," Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)

set1 = {'PDGBA', "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ,"Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)
mydict = {
"brand": "Nokia", # key value pair
"model": "premium",
"year": 2010
}
print(mydict)

# Access the Elements of Dictionary
a = mydict["model"]
print(a)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict. Keys ()
print(x)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict. Keys()
print(x)

mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict.keys()
print(x)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict.values()
print(x)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,   # change the product year 2018 to 2020
}
mydict["year"] = 2020
print(mydict)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
mydict ["price"] = 5000 # adding price in the dictionary
print (mydict)
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2023
}
del mydict["year"] # use of del keyword
print(mydict)

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear () # use of clear ( ) method
print(thisdict)


mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict1 = mydict.copy() # use of copy method
print(mydict1)
a =1 
while a < 11:
    print (5,"X",a,"=",a*5)
    if a == 6 :
        break
    a += 1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # continue statement
    print (i)

course = ["Car", "Motorcycle", "Bicycle"]
student = ["John", "Shelly", "Mike"]
for x in course:
    for y in student:
        print(x, y)

for i in range(0,6):
    print("*")

for i in range(0,6):
    for j in range(i , 6):
        print("*")

for i in range(1,6):
    for j in range(i , 6):
        print(i*"*")

for i in range(1,6):
    for j in range(i , 6):
        print(i+"*")

for i in range(1,6):
    print(i*"*")

for i in range(1,6):
    print("\t",i*"*")

for i in range(1,6):
    print(i*"*")

def my_func(str):
    print(str+"Engineering")

my_func("Chemical")
my_func("Biotech")
my_func("Information Technology")

def my_func(str):
    print(str+" Engineering")

my_func("Chemical")
my_func("Biotech")
my_func("Information Technology")

def add(a,b):
    x = a+b
    return x

print("Addition of two number 9 and 15 is :" , add(9, 15))

def my_function(*data):
    
    print ("The details is " + data[1])

my_function ("Email", "Contact_no", "Address")
def my_function(*data):
    print ("The details is " + data[1])
my_function ("Email", "Contact_no", "Address")

def primordials(seeds):
    for x in seeds:
        print(x)

daemon = ["Rouge","Noir","Blanc","Jaune","Violet","Vert","Bleu"]
primordials(daemon)

def add(a,b):
    x = a+b
    print("Addition of ",a," and ", b ," is :" , x)

add(34, 35)

def multiple(x):
    return x*7

print(multiple(9))



cube_v2 = lambda x : x*x*x
print (cube_v2(7))



def func1():
    pass

salutaion = lambda : print("Hello User!!")
salutaion()

str = input("Enter a String to convert it into upper case : ")
upper = lambda string : string.upper()
print(upper(str))


test = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list (filter (lambda x: (x % 2 != 0), test))
print(final_list)

var = input("Enter an integer for increment")
x = lambda a : a+5
print(x(10))

var = input("Enter an integer for increment : ")
x = lambda a : a + 5
print(x(10))

var = input("Enter an integer for increment : ")
x = lambda a : a + 5
print(x(var))

var = int(input("Enter an integer for increment : "))
x = lambda a : a + 5
print(x(var))

x = lambda a , b : a*b 
print(x(3*23))

x = lambda a , b : a*b 
print(x(3,23))


x = lambda a , b : a*b 
print(x(3,25))

x = lambda a, b, c: a + b * c
print (x(5, 6, 2))
item = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final = list(map(lambda x: x*2, item))
print(final)

Max = lambda a, b : a if(a > b) else b
print("The Result is:", Max(5, 34))
list = []
l = int(input("Enter the Length of List : "))
for i in range(0,l):
    x= int(input("Enter the ", i," index element of list : "))
    list = list.append(x)

print(list)
list = []
l = int(input("Enter the Length of List : "))
for i in range(0,l):
    x= int(input("Enter the element of list : "))
    list = list.append(x)

print(list)
9
list = []
l = int(input("Enter the Length of List : "))
for i in range(0,l):
    list[i] = int(input("Enter the element of list : "))


print(list)
list = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    list[i] = int(input("Enter the element of list : "))
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    list1=list1+[i]
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1=list1+[values]


print(list1)
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1=list1.append(values)


print(list1)
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1=list1.extend(values)


print(list1)
 Lambda function on custom input list
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1.append(values)


print(list1)

list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1.append(values)


print(list1)
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1.append(values)


print(list1)
list2 = list(map(lambda x : x*2 , list1))
print(list2)
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list at index ",i,": "))
    list1.append(values)

print(list1)
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list at index : "))
    list1.append(values)

print(list1)

class Demo:
    # Class attribute
    institute = "CDAC"
    # instance attribute
    def __init__(self,name):
        self.name = name
        def course(self):
            print("My Course is {}".format(self.name))
Shaswat = Demo("Pgdbda")

class Demo:
    # Class attribute
    institute = "CDAC"
    # instance attribute
    def __init__(self,name):
        self.name = name
        def course(self):
            print("My Course is {}".format(self.name))
Shaswat = Demo("Pgdbda")
Shaswat.course
runfile('C:/Users/marmi/.spyder-py3/Class Script.py', wdir='C:/Users/marmi/.spyder-py3')

class Demo:
    # Class attribute
    institute = "CDAC"
    # instance attribute
    def __init__(self,name):
        self.name = name
    def course(self):
        print("My Course is {}".format(self.name))
# Object Created
Shaswat = Demo("Pgdbda")
# Accessing the class methods
Shaswat.course()
runcell(0, 'C:/Users/marmi/.spyder-py3/Class Script.py')
runfile('C:/Users/marmi/.spyder-py3/Class Script.py', wdir='C:/Users/marmi/.spyder-py3')
runfile('C:/Users/marmi/.spyder-py3/Class Script.py', wdir='C:/Users/marmi/.spyder-py3')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE : " + self.age)
p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE : " , self.age)
p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE :" , self.age)
p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE :" ,self.age)
p1 = Person("John", 36)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE :" ,self.age)
p1 = Person("John", 36)
p1.myfunc()

class Person(object):
# __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

# child class
class Employee(Person):
    
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
# invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        print("Salary : {}".format(self.salary) )

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using
# its instance
a.display()
a.details()

class Employee(Person):
    
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
# invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        print("Salary : {}".format(self.salary) )

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using
# its instance
a.display()
a.details()

class Employee(Person):
    
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
# invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        print("Salary : {}".format(self.salary) )

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
# calling a function of the class Person using
# its instance
a.display()
a.details()

t1 = (('a',1),('b',2),('c',3))
d1 = dict(t1)
print(d1)

lot = [('Justice','Michael'),('Purity','Metatron'),('Wisdom','Raphael'),('Hope','Sariel'),('Patience','Gabriel'),('Covenant','Uriel'),('Charity','Raghuel')]
lod = dict(lot)

lot = [('Justice','Michael'),('Purity','Metatron'),('Wisdom','Raphael'),('Hope','Sariel'),('Patience','Gabriel'),('Covenant','Uriel'),('Charity','Raghuel')]
lod = dict(lot)
print(lod)

keys= ["Wrath","Pride","Gluttony","Sloth","Lust","Greed","Envy"]
values= ["Satan","Lucifer","Belzebuth","Belphaghor","Astaroth","Mammon","Leviathan"]
hell = dict(zip(keys,values))
print(hell)
pip install numpy
runfile('C:/Users/marmi/.spyder-py3/Numpy Script.py', wdir='C:/Users/marmi/.spyder-py3')
import numpy as np
print(np.__version__)
pip update numpy
pip insatall numpy
pip install numpy
a = np.array(1,2,3,4)
print(a)
type(a)
a[2]
a[1]
import numpy as np
print(np.__version__)


a = np.array(1,2,3,4)
print(a)
type(a)
a[2]
a[1]
runfile('C:/Users/marmi/.spyder-py3/Numpy Script.py', wdir='C:/Users/marmi/.spyder-py3')
class MyError(Exception):
# Constructor or Initializer
    def __init__(self, value):
        self.value = value
# __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

try:
    raise(MyError(3*2))
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)
print(var)
runfile('C:/Users/marmi/.spyder-py3/Numpy Script.py', wdir='C:/Users/marmi/.spyder-py3')

zero = np.array(92)
print(zero)
print(type(zero))

oneD = np.array([2,4,6,8,9])
print(oneD)

twoD = np.array([[2,4,5,6,8,10,12,14],[1,3,5,7,9,11,13]])
print(twoD)


twoD = np.array([[2,4,5,6,8,10,12,14],[1,3,5,7,9,11,13]])
print(twoD)

twoD = np.array([[2,4,5,6,8,10,12,14],[1,3,5,7,9,11,13,15]])
print(twoD)

threeD = np.array([[[1,2,3],[4,5,6]],[7,8,9],[10,11,12]])
print(threeD)

threeD = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(threeD)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

twoD = np.array([[2,4,5,6,8,10,12,14],[1,3,5,7,9,11,13,15]])   

''' The no. of elements in the columns should be same 
otherwise it will be inhomogeneous 
and will throw ValueError'''

print(twoD)
print("Array Dimension : " , twoD.ndim)
runfile('C:/Users/marmi/.spyder-py3/Exception Handling Script.py', wdir='C:/Users/marmi/.spyder-py3')

item = [15, 17, 30] 
try:  
  print ("Secod element = %d" %(item[1])) 
  
  # Throws error since there are only 3 elements in array 
  print ("Fourth element = %d" %(item[3])) 

except: 
    print ("An error occurred")
runfile('C:/Users/marmi/.spyder-py3/Pandas.py', wdir='C:/Users/marmi/.spyder-py3')


d1 = {"Rouge" : "Guy Crimson","Noir" : "Diablo","Blanc" : "Testarossa","Jaune" : "Carrera",
      "Violet" : "Ultima","Vert" : "Raine","Bleu" : "Miseri"}

ser = pd.Series(d1)
print(ser)
runfile('C:/Users/marmi/.spyder-py3/Data Frame.py', wdir='C:/Users/marmi/.spyder-py3')
runfile('C:/Users/marmi/.spyder-py3/Series Script.py', wdir='C:/Users/marmi/.spyder-py3')
import pandas as pd
import numpy as np

info = np.array(['P','a','n','d','a','s'])
s = pd.Series(info)
print(s)
runfile('C:/Users/marmi/.spyder-py3/Pandas.py', wdir='C:/Users/marmi/.spyder-py3')

x = pd.Series(4,[0,1,2,3])
print(x)

x = pd.Series("P",["Vansh","Saket","Nipun","Kamesh"])
print(x)

data = np.array(['C','D','A','C','D','E', 'L','H','I','J','A','S','O','L','A'])
ser1 = pd.Series (data)
print (ser1[2:7])       # for retrieve the elements, slice method used

data = np.array(['C''D''A''C','D','E','L','H','I'])
ser = pd.Series(data, index=[1,2,3,4,5,6,7,8])
print (ser[6])

data = np.array(['C''D''A''C','D','L','H','I'])
ser = pd.Series(data, index=[1,2,3,4,5,6,7,8])
print (ser[6])

data = np.array(['C''D''A''C','D','L','H','I'])
ser = pd.Series(data, index=[1,2,3,4,5,6,7,8])

data = np.array(['C','D','A','C','D','L','H','I'])
ser = pd.Series(data, index=[1,2,3,4,5,6,7,8])
print (ser[6])

## ---(Sun Oct 20 20:09:38 2024)---


import pandas as pd

# Reading csv file from source
data = pd.read_csv('C:\\Users\\marmi\\OneDrive\\Documents\\cars_data.csv')

print(data)
hort_data = data.head () # creating short data of 5 rows
short_data = data.head ()


import pandas as pd

# Reading csv file from source
data = pd.read_csv('C:\\Users\\marmi\\OneDrive\\Documents\\cars_data.csv')

print(data)

short_data = data.head ()


import pandas as pd

# Reading csv file from source
data = pd.read_csv('C:\\Users\\marmi\\OneDrive\\Documents\\cars_data.csv')

print(data)

short_data = data.head () # creating short data of 5 rows
print(short_data)
runfile('C:/Users/marmi/untitled5.py', wdir='C:/Users/marmi')
perations

import pandas as pd

# Reading csv file from source
data = pd.read_csv('C:\\Users\\marmi\\OneDrive\\Documents\\cars_data.csv')

print(data)

short_data = data.head () # creating short data of 5 rows
print(short_data)


import pandas as pd

# Reading csv file from source
data = pd.read_csv('C:\\Users\\marmi\\OneDrive\\Documents\\cars_data.csv')

print(data)

short_data = data.head () # creating short data of 5 rows
print(short_data)
runfile('C:/Users/marmi/untitled5.py', wdir='C:/Users/marmi')
print(short_data.to_string()) # to print whole data_frame

## ---(Wed Oct 23 11:30:43 2024)---
pip install mysql-connector-python
runfile('C:/Users/marmi/DatabaseConnectionWIthPython.py', wdir='C:/Users/marmi')
runfile('C:/Users/marmi/.spyder-py3/DatabaseConnectionWIthPython.py', wdir='C:/Users/marmi/.spyder-py3')

## ---(Wed Oct 23 11:52:21 2024)---
runfile('C:/Users/marmi/.spyder-py3/DatabaseConnectionWIthPython.py', wdir='C:/Users/marmi/.spyder-py3')

## ---(Wed Oct 23 12:07:53 2024)---
runfile('C:/Users/marmi/.spyder-py3/DatabaseConnectionWIthPython.py', wdir='C:/Users/marmi/.spyder-py3')
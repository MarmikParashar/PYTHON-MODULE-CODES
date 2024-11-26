# Class Creation
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

# Example 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object Creation in Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
        print("AGE :" ,self.age)
p1 = Person("John", 36)
p1.myfunc()

# Self Parimeter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Inheritance

# parent class
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
# First Funtion
def my_func(str):
    print(str+" Engineering")

my_func("Chemical")
my_func("Biotech")
my_func("Information Technology")

# Function with arguments
def add(a,b):
    x = a+b
    print("Addition of ",a," and ", b ," is :" , x)

add(34, 35)

# Arbitrary Arguments
def my_function(*data):
    print ("The details is " + data[1])
my_function ("Email", "Contact_no", "Address")

# Passing a List as Argument
def primordials(seeds):
    for x in seeds:
        print(x)

daemon = ["Rouge","Noir","Blanc","Jaune","Violet","Vert","Bleu"]
print("Rulers of Daemon Realm : ")
primordials(daemon)

# Return Statements
def multiple(x):
    return x*7

print(multiple(9))

# Pass Statement
# Used for defining funtion definition with no content
def func1():
    pass

# Anonymus Function
# It is Defined With the help of Lambda Funtion
# using lambda function
cube_v2 = lambda x : x*x*x
print (cube_v2(7))



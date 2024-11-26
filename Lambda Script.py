# Basic Syntax
salutaion = lambda : print("Hello User!!")
salutaion()

# Lambda funtion for converting a string to upper case
str = input("Enter a String to convert it into upper case : ")
upper = lambda string : string.upper()
print(upper(str))

# Lambda funtion for filtering list to get odd no. list
test = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list (filter (lambda x: (x % 2 != 0), test))
print(final_list)

# Lambda function for increment
var = int(input("Enter an integer for increment : "))
x = lambda a : a + 5
print(x(var))

# Lambda funtion with two arguments
x = lambda a , b : a*b 
print(x(3,25))

# Lambda function with three arguments
x = lambda a, b, c: a + b * c
print (x(5, 6, 2))

# Lambda function for Map
item = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final = list(map(lambda x: x*2, item))
print(final)

# use of lambda function with if -else
Max = lambda a, b : a if(a > b) else b
print("The Result is:", Max(5, 34))

# Lambda function on custom input list
list1 = []
l = int(input("Enter the Length of List : "))
for i in range(l):
    values=int(input("Enter The values of list : "))
    list1.append(values)
    
print(list1)
list2 = list(map(lambda x : x*2 , list1))
print(list2)
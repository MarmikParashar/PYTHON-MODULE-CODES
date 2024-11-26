# =============================================================================
# 
# # initialize the amount variable 
# amount = 10000
#   
# # perform division with 0 
# amount = amount/ 0
# print(amount)
# 
# 
# =============================================================================


# =============================================================================
# x = 50
# y = "hello"
# z = x + y 
# =============================================================================


x = 5
y = "hello"
try: 
    z = x + y 
except TypeError: 
    print("Error: cannot add an int and a str") 
    
    
## Try Expepct
item = [15, 17, 30] 
try:  
  print ("Secod element = %d" %(item[1])) 
  
  # Throws error since there are only 3 elements in array 
  print ("Fourth element = %d" %(item[3])) 
  
except: 
    print ("An error occurred") 
    
# Division by Zero Exception
# Example 1
def divide(p , q): 
   try: 
        c = ((p+q) / (p-q)) 
   except ZeroDivisionError: 
        print ("p/q result in 0") 
   else: 
        print (c) 
  
divide(6.0, 6.0) 

# Example 2
try: 
    k = 5//0  # raises divide by zero exception. 
    print(k) 
  
# handles zerodivision exception 
except ZeroDivisionError: 
    print("Can't divide by zero") 
  
finally: 
    # this block is always executed 
    # regardless of exception generation. 
    print('This is always executed') 
    
    
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
    
a=10
b=0
try:
    print ("This is outer try block")
    try:
        print (a/b)
    except ZeroDivisionError:
        print ("Division by 0")
    finally:
        print ("inside inner finally block")

except Exception:
    print ("General Exception")
finally:
    print ("inside outer finally block")

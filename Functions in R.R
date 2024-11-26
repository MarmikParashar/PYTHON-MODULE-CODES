# R -Function'

student <- function(){
  print("hello")
}
student()

# function with argument
student <- function(fname,lname){
  paste(fname,lname)
}
student("Amit","Kumar")
student("sumit","kumar")

# Return any value

my_function <- function(x) {
  return (5 * x)
}

print(my_function(3))
print(my_function(5))
print(my_function(9))

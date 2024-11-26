#R - Decision making

#if condition - statement

x <- 60

if(x > 45){ 
  print(paste(x, "is greater than 10")) 
}


# if-else statement

a <- 200
b <- 330

if (b > a) {
  print("b is greater than a")
} else {
  print("b is not greater than a")
}
# if use with or AND 

a <- 200
b <- 33
c <- 500

if (a > b & c > a) {
  print("Both conditions are true")
}
#if-elseif -else

a <- 50
b <- 75
c <- 93

if(a > b && b > c)
{
  print("condition a > b > c is TRUE")
} else if(a < b && b > c)
{
  print("condition a < b > c is TRUE")
}else if(a < b && b < c)
{
  print("condition a < b < c is TRUE")
}else
{
  print("All inputs are invalid")
}
#switch statement: If no case is matched it outputs NULL 
x <- "apple"

result <- switch(x,
                 apple = "It's an apple.",
                 banana = "It's a banana.",
                 orange = "It's an orange."
)

print(result)
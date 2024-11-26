# while loop

i <- 1
while (i < 6) {
  print(i)
  i <- i + 1
  print(i)
}

#repeat loop
x = 2

# Print 1 to 10
repeat{ 
  print(x) 
  x = x + 2
  if(x > 8){ 
    break
  } 
}

#next statement:used to skip the current iteration without executing the further statements 
# Defining vector 
x <- 1:10

# Print even numbers 
for(i in x){ 
  if(i%%2 != 0){ 
    next #Jumps to next loop 
  } 
  print(i) 
}
#for loop

for (i in 3: 12)
{
  print(i ^ 2)
}

# break statement

i <- 1
while (i < 6) {
  
  i <- i + 1
  if (i == 4) {
    break
  }
  print(i)
}
# R Data Structures
student <- c("Sumit","Amit","Tarun","Vikas")  # String values
student
# Numerical values
age <- c(25,35,45)
age
# to print a sequence
number <- 20:25
number
# to print using decimal number
number <- 2.75:5.5
number
#to print logical values
result <- c(TRUE, FALSE, TRUE)
result
# find the length of vector
length(result)
# sort the vector
sort(student)
# Accesing the one element 
student[2]
# Accesing the many elements at a time
student[c(1, 3)]
# changing item in the vector
student[2]= "sunil"
student

# R -List
mylist <- list("grapes","Banana","Orange")
mylist
# access list using index
mylist[2]
# Change Item Value
mylist[3]= "guava"
mylist
length(mylist)
# check the specific item exist or not
"Orange" %in% thislist

# add any item to the end of list
append(student,"lichi")
# add any item to the list to a specific position
mylist2 <- list("BCA","MCA","MTech")
mylist2
append(mylist2,"BTech", after=2)
# Remove item from the list:
thislist <- list("apple", "banana", "cherry")

newlist <- thislist[-1]

# Print the new list
newlist
# To find the specify a range of items
thislist <- list("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

(thislist)[2:5]
# Join Two Lists

list1 <- list("a", "b", "c")
list2 <- list(1,2,3)
list3 <- c(list1,list2)

list3
# Create a matrix
thismatrix <- matrix(c(20,25,30,40,50,60), nrow = 2, ncol = 4)

# Print the matrix
thismatrix
# Access the matrix items

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix
thismatrix[2, 1]

# accessing only whole column

thismatrix <- matrix(c("apple", "banana", "cherry", "orange"), nrow = 2, ncol = 2)
thismatrix[,2]
# accessing more than one column

thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)
thismatrix
thismatrix[, c(1,2)]
# Use the cbind() function to add additional columns in a Matrix:
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)

newmatrix <- cbind(thismatrix, c("strawberry", "blueberry", "raspberry"))

# Print the new matrix
newmatrix

# rbind() function to add additional rows in a Matrix:
thismatrix <- matrix(c("apple", "banana", "cherry", "orange","grape", "pineapple", "pear", "melon", "fig"), nrow = 3, ncol = 3)

newmatrix <- rbind(thismatrix, c("strawberry", "blueberry", "raspberry"))

# Print the new matrix
newmatrix

# Remove Rows and Columns
thismatrix <- matrix(c("apple", "banana", "cherry", "orange", "mango", "pineapple"), nrow = 3, ncol =2)

#Remove the first row and the first column
thismatrix <- thismatrix[-c(1), -c(1)]

thismatrix
# to find the no of rowas and col in a natriix
dim(newmatrix)

# Combine matrices
Matrix1 <- matrix(c("apple", "banana", "cherry", "grape"), nrow = 2, ncol = 2)
Matrix2 <- matrix(c("orange", "mango", "pineapple", "watermelon"), nrow = 2, ncol = 2)

# Adding it as a rows
Matrix_Combined <- rbind(Matrix1, Matrix2)
Matrix_Combined

# Adding it as a columns
Matrix_Combined <- cbind(Matrix1, Matrix2)
Matrix_Combined

# R-array
thisarray <- c(1:24)      # single dimension array
thisarray
# More than one dimension array
multiarray <- array(thisarray, dim = c(4, 3, 2))
multiarray

# R-Data frame
sunil <- data.frame (
  student = c("Amit","Sumit","Tarun","Vivek"),
  age = c(25,30,35,50),
  course =c("BCA","MCA","B.Tech","MTech")
)
sunil

# Summarize the Data
summary(sunil)
test1 <- data.frame(
  course = c("BCA","MCA","BTech","M.Tech"),
  Age = c(25,30,28,40),
  addr = c("Delhi","Meerut","Khatauli","Noida")
)
test1[1]     # by using single bracket
test1[["course"]] # By using [[]] double bracket
test1$course   # By using $ sign
# add rows  rbind()
school <- rbind(test1,c("DPS","MPS","DDPS","RKGIT"))
school
test1
# add new column in a data frame cbind()
name <- cbind(test1,name = c("Sumit","mohit","tarun","vikas"))
name
# Remove Rows and Columns
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

# Remove the first row and column
Data_Frame_New <- Data_Frame[-c(1), -c(1)]
Test_new <- test1[-c(1),]
# Print the new data frame
Test_new
# Amount of Rows and Columns
dim(test1)
# ncol() columns and nrow() to find the number of rows:
ncol(test1)
nrow(test1)
# to find the number of column :
length(test1)
# Combining Data Frames

sunil <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

amit <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)

New_Data_Frame <- rbind(sunil, amit, test1)
New_Data_Frame


# R-Factor

# Create a factor
course <- factor(c("BCA", "MCA", "BSc", "MSc", "BTech"))

# Print the factor
course
# to print only levels
levels(course)
# find the no of items using length()
length(course)

# acees item from factor 
course[3]
# change the value of a specific item
course[1]<- "PHD"
course
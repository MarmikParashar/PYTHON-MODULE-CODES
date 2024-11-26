#R Basic
myString <- "Hello, Delhi!"
print ( myString)

# comments
if(FALSE) {
  "This is a demo for multi-line comments and it should be put inside either a 
      single OR double quote"
}
myString <- "Hello, World!"
print ( myString)

# Variable declaration and value assignment

name <- "John"
age <- 40

name   # output "John"
age    # output 40

# concatenating the variable
text <- "awesome"

paste("R is", text)

#adding two variables
text1 = "Bigdata"
text2 = "Technology"
paste(text1,text2)

#adding two variables different datatypes
text1 = "Bigdata"
text2 = "24"
paste(text1+text2) # will generate error

# Assigining one values to multiples variables
Height<-age<-weight<-40
Height
my_var <- 30 # my_var is type of numeric
my_var <- "Sally" # my_var is now of type character (aka string)
# to find the class of data
x <- 10.5
class(x)

# integer
x <- 1000L
class(x)

# complex
x <- 9i + 3
class(x)

# character/string
x <- "R is exciting"
class(x)

# logical/boolean
x <- TRUE
class(x)

#Type Conversion

x <- 1L # integer
y <- 2 # numeric

# convert from integer to numeric:
a <- as.numeric(x)
class(a)

# convert from numeric to integer:
b <- as.integer(y)
b

# print values of x and y
x
y

# print the class name of a and b
class(a)
class(b)

# Built-in Math Functions
max(10,15,20)
min(10,15,20)
abs(-5.9)
ceiling(3.2)
floor(2.4)

# Assign a String to a Variable
str <- "CDAC"
str
# Assign a multiline String to a Variable
str <- "Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."
cat(str)
#  check if a character or a sequence of characters are present in a string

str <- "Hello World!"

grepl("H", str)
grepl("Hello", str)
grepl("X", str)

# booleans operations 
10 > 9 

#Data Types
# Create a vector.
apple <- c('red','green',"yellow")
print(apple)
# Get the class of the vector.
print(class(apple))


# Create a list.
list1 <- list(c(2,5,3),21.3,sin)

# Print the list.
print(list1)

# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
M
print(M)

# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,3)) 
# First parameter for row and second for column and third is for how many number of array to be create
print(a)

# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')
apple_colors

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))
i
# Create the data frame.
BMI <- 	data.frame(
  gender = c("Male", "Male","Female"), 
  height = c(152, 171.5, 165), 
  weight = c(81,93, 78),
  Age = c(42,38,26)
)
print(BMI)


#R - Operators
#1.Colon operator.creates the series of numbers in sequence for a vector
a <- 2:8
print(a)
#2.%in%: used to identify if an element belongs to a vector
v1 <- 8
v2 <- 12
t <- 1:10
print(v1 %in% t) 
print(v2 %in% t) 

#3 %*%: to multiply a matrix with its transpose

M = matrix( c(2,6,5,1,10,4), nrow = 2,ncol = 3,byrow = TRUE)
print(M)
t = M %*% t(M)
print(t)

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

# R-Plotting
plot(2,3)    # single point plotting
# more than one  point plotting
plot(c(2,8,6,7,5),c(3,9,6,7,8))
# using labels name

name <- c("Sunil","Amit","Tarun","vishal")
age <- c(25,30,35,40)
plot(name,age)
# draw a line

plot(1:10, type="l")
# Create a vector of pies
x <- c(10,20,30,40)

# Display the pie chart
pie(x)

# adding angle in pie
pie(x, init.angle = 70)

#Reading & Importing data from Text files, Excel files

# Read a CSV file
data <- read.csv("C:/Users/marmi/OneDrive/Documents/cars_data.csv")
print(data)

#Analyzing the CSV File
print(is.data.frame(data))

# to find the nuber of colum
print(ncol(data))

# to Find the Number of rows
print(nrow(data))

# Exporting data in CSV  file

data <- read.csv("E:/data/student2.csv", header=TRUE)
sub<-data["age"]
print(sub)
newframe<-write.csv(sub,"new1.csv", row.names = FALSE)

# Read Excel file 

install.packages("xlsx")
library(readxl)
library(xlsx)

data <-read_xlsx("E:/data/split3.xlsx")
write.xlsx(sub ,"new5.xlsx", row.names = FALSE)
newframe <- read.xlsx("new5.xlsx")
print(newframe)

# display data
newf <- read.csv("E:/data/student.csv")
print(newf)
write.csv(newf,"output13.csv", row.names = FALSE)

# Extracting columns from csv data set 
data <-read.csv('E:/data/student.csv')
df2 <-data[, c("age", "absences","gender")]  
print(df2)  
write.csv(df2,"output34.csv", row.names = FALSE)

###
gfg_data <- fread("E:/data/student.csv",select = c("age", "gender", "absences")) 
gfg_data
write.csv(gfg_data,"output35.csv", row.names = FALSE)

################## read multiple csv file and merge s
install.packages("dplyr")
install.packages("readr")
install.packages("plyr")
library(purrr) 
library(dplyr) 
library(readr)
 
data<-list.files(path="E:/data/", pattern="*.csv", full.names= "TRUE")%>%
  lapply(read_csv)%>% bind_rows()
new_df<-as.data.frame(data)
write.csv(new_df,"output45.csv", row.names = FALSE)
new_df
getwd()


############# read multiple text file in R 

library(parallel) 
file_list <- c("a.txt","b.txt","ca.txt") 
path <- "C:/Users/PRAVEEN/OneDrive/Desktop/PGDBDA/"
file_list <- paste0(path, file_list) 

extract_data_from_file <- function(file) { 
  data <- readLines(file) 
  return(data)
} 
files <- list.files(pattern = ".txt")
cl <- makeCluster(detectCores()) 
results <- parLapply(cl, file_list,extract_data_from_file) 
stopCluster(cl) 
print(results)

###################### merging of two dataframe from a CSV file
data <-read.csv('E:/data/student.csv')
df2 <-data[, c("age", "absences","gender")]  
print(df2)  
df3 <-data[, c("age", "absences","gender")]  
df3
df4<-rbind(df2,df3)  
################## Reshaping the data transpose of a Matrix
mat <- matrix(c(5:35),nrow=4,byrow=TRUE)  
mat 
print("Matrix after transpose\n")  
m1 <- t(mat)  
m1  

## melting
install.packages("MASS")
install.packages("reshape2")
library(MASS)  
library(reshape2)  
molten_ships <- melt(ships, id = c("type","year"))  
print(molten_ships)  
# Mergin the dataframe
library(MASS)
merged.Pima <- merge(x = Pima.te, y = Pima.tr,
                     by.x = c("bp", "bmi"),
                     by.y = c("bp", "bmi")
)
print(merged.Pima)
nrow(merged.Pima)

###melt and cast() function
install.packages("MASS")
install.packages("reshape2")
install.packages("reshape")
library(MASS)  
library(reshape2) 
library(reshape)

#Melting the data  in dataframe
diab<-read.csv('E:/data/diab.csv')
datanew <- melt(diab, id = c("Glucose","Age"))  
write.csv(datanew,"output45.csv", row.names = FALSE)
print(datanew)  

#Casting of data in another shape 
library(MASS)  
library(reshape2) 
library(reshape)
cast_data<-cast(datanew,'Age~variable',sum)  
write.csv(cast_data,"output67.csv", row.names = FALSE)
print(cast_data)  

## sort a Dataframe 
data <-read.csv('E:/data/student.csv')
dfn <-data[, c("age", "absences","gender","name")]  
print(dfn)
# decreasing order based on age
print(data[order(dfn$name, decreasing = TRUE), ])
write.csv(dfn,"output18.csv", row.names = FALSE)

#sort the data in increasing order based on age
print(data[order(data$name, decreasing = FALSE), ])
write.csv(dfn,"output19.csv", row.names = FALSE)

# arrange method in increasing order
library("dplyr") 
data <-read.csv('E:/data/student.csv')
dfn <-data[, c("age", "absences","gender","name")] 
write.csv(dfn,"output21.csv", row.names = FALSE)
print(arrange(dfn, gender))

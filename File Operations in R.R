#Reading & Importing data from Text files, Excel files

# Read a CSV file
data <- read.csv("E:/data/student.csv")
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
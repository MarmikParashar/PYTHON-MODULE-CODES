
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
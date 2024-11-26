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
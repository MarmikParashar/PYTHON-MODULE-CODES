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
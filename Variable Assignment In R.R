
# Assign a String to a Variable
str <- "CDAC"
str

# Assigining one values to multiples variables
Height<-age<-weight<-40
Height
my_var <- 30 # my_var is type of numeric
my_var <- "Sally" # my_var is now of type character (aka string)

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
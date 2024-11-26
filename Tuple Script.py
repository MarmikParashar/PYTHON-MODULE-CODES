# tuples is list
mytuples = ("Orange","Apple","Banana")
print(mytuples)

# by using single items
mytuples = ("Orange",)
print(mytuples)

# different types of data in tuples
mytuples = ("Orange",25,True)
print(mytuples)

# Operatin On Tuples

# Access Tuple Items

mytuple = ("Roughe","Noir","Blanc")
print(mytuple)
# Index Method for accessing tuples
tuple1 = ("White","Red","Black","Yellow")
print(tuple1[3])
# Index range method
print(tuple[1:3])

# Change the items of tuple
a = ("Noir","Blanc","Violet","Jaune") 
b = list(a)
#b[2]= "Rouge"
b.extend(["Rouge","Vert","Bleu"])
a = tuple(b)
print(a)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry") # Packing process
(green, yellow, red) = fruits # unpacking
print (green)
print (yellow)
print (red)

mycourse = ("BCA", "BBA", "MBA", "MCA", "MTech")
(amit, sumit,*vaibhav, tarun) = mycourse
print(amit)
print(sumit)
print(*vaibhav)
print(tarun)

# Print Tuple Items Using Loop
mycourse = ("BCA", "BBA", "MBA", "MCA", "MTech")
for x in mycourse: # for loop
    print(x)
    
# Join Two Tuples
t1 = ("Justice","Covenant","Hope","Charity","Patience","Purity","Wisdom")
t2 = ("Judgement","Heaven","Dominion","Trials","Salvation","Glory","Rigor")
t3 = t1+t2
print(t3)



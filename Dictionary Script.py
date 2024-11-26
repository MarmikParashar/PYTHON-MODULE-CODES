# Dictionary Creation
mydict = {
"brand": "Nokia", # key value pair
"model": "premium",
"year": 2010
}
print(mydict)

# Access the Elements of Dictionary
a = mydict["model"]
print(a)

# Finding the Keys in Dictionaries
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict.keys()
print(x)

# Finding the Values in Dictionaries
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
x= mydict.values()
print(x)

# Change Dictionary Items
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,   # change the product year 2018 to 2020
}
mydict["year"] = 2020
print(mydict)

# Adding Items in the dictionary
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2018,
}
mydict ["price"] = 5000 # adding price in the dictionary
print (mydict)

# Remove Dictionary Items

# pop (“items”) method: it will remove the specific item by using they item keys.
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2023
}
mydict.Pop("model") # pop ( ) method use   
print (mydict)

'''popitem ( ): This method will remove the last inserted item. 
In version 3.7 will do similarly while below 3.7 version it will
remove the random item from the dictionary.'''

mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2023

}
mydict.popitem()
print(mydict)

# del keyword: Del keyword is removes the item with the Specified Key name

mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2023
}
del mydict["year"] # use of del keyword
print(mydict)

# Deleting the entire Dictionary
mydict = {
"brand": "Nokia",
"model": "Premium",
"year": 2023
}
del mydict      # use of del keyword for deletion of dictionary.

# Empty the dictionary: 
    
# Clear () method can be used to empty the dictionary.
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear () # use of clear ( ) method
print(thisdict)

# Copy the dictionary: 
# copy ( ) method 
mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict1 = mydict.copy() # use of copy method
print(mydict1)

# [Note: dict ( ) function also can be used for creating a copy of the dictionary.]

# Dictionary Creation using list and tuples

# From tuple of tuples
t1 = (('a',1),('b',2),('c',3))
d1 = dict(t1)
print(d1)

# From list of tuples
lot = [('Justice','Michael'),('Purity','Metatron'),('Wisdom','Raphael'),('Hope','Sariel'),('Patience','Gabriel'),('Covenant','Uriel'),('Charity','Raghuel')]
lod = dict(lot)
print(lod)

# Using two Lists
keys= ["Wrath","Pride","Gluttony","Sloth","Lust","Greed","Envy"]
values= ["Satan","Lucifer","Belzebuth","Belphaghor","Astaroth","Mammon","Leviathan"]
hell = dict(zip(keys,values))
print(hell)
                                                                                           




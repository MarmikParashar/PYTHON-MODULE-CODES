# set
myset = {"Myschool","Books","Books"}
print(myset)

#enth of a set
myset = {"school","class","Exam","Result"}
print(len(myset))

#acees the elements from a set using in keyword
myset = {"school","class","Exam","Result"}
for x in myset:
    print(x)
    
    
#add items in the set
myset = {"school","class","Exam","Result"}
myset.add("Test")
print(myset)

# Adding a Set to another set
set1 = {"Wrath","Pride","Gluttony","Lust","Envy","Sloth","Greed"}
set2 = {"Death","Poison","Temptation","Annihilation"}
set1.update(set2)
print(set1)

# Remove items
    
# remove() method  Note: if the requested item does not exist then it will raise an error
myset = {"school","class","Exam","Result"}
myset.remove("class")
print(myset)
# discard() method Note: if the requested item does not exist then it will not raise an error
myset = {"BBA", "BCA", "B.Tech"}
myset.discard("BCA")    # discard( ) method
print(myset)

'''pop() method     [Note: Set is unordered. Pop () method 
will remove a random item from set, 
so we cannot be sure which item will be removed.'''

myset = {"BBA", "BCA", "B.Tech"}
myset.pop( )

# Empty the Set
# clear() method    It will leave the Set empty but leave its Structure
s= {"school","class","Exam","Result"}
print(s)
s.clear()
print(s)

# Delete the Set
s1 = {"Myschool","Books","Books"}
print(s1)
del s1

# Join Sets
# Union Method  It is used for creating a new Set from the two sets

set1 = {"PDGBA", "PGDAC" , "PGDIT", "CDAC"}
set2 = {'Amit', "Tarun", "Mohit", "CDAC"}
set3 = set1.union (set2) # union () method
print (set3)

# Update Method     It will add the elements of one set in another set
set1 = {'PDGBA', "PGDAC" ,"PGDIT" , "Markile"}
set2 = {'Amit', "Tarun", "Mohit" ,"Markile"}
set2 = set1.update (set2) # update ( ) method
print (set1)




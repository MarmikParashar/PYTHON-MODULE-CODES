# list 
mylist = ["Sports","Education","Seminar"]
print(mylist)

# length of a list
print(len(mylist))

mylist = [True,False,True]
print(mylist)

# different type of data 
mylist = ['Apple',23,True]
print(mylist)

# accesing items from the list

mylist = ["Sports","Education","Seminar","School"]
print(mylist[3])         # listname[indexno]

# Negative indexing
mylist = ["Sports","Education","Seminar","School"]
print(mylist[-4])

# access items by using range of index

mylist = ["Sports","Education","Seminar","School","Btech","MCA"]

#print(mylist[2:5])     # listname[startrange:end range]
#print(mylist[:5])
#print(mylist[3:])
#print(mylist[-3:-1])

# to checl any specific items exits in the list using in keyword

if "Seminar" in mylist:
    print("Yes")
    
# to change the item value 
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist[0]="Timetable"      # listname[indexno]="value"
print(mylist)

# To make chnage by using range value
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist[2:4] = ["Mr.John","Alex"]
print(mylist)

# insert items in a list  insert()
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.insert(2,"Practice")     # insert(indexno,"value")
print(mylist)

# appned mehtod to insert   listname.append("value")
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.append("BCA")
print(mylist)

# extend a list from one list to another list
list1 =["BBA","BCA","MCA"]
list2 = ["25K","35K","65K"]
list1.extend(list2)
print(list1)

# Remove the items from a list
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.remove("Sports")
print(mylist)

# remove items by using pop method
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.pop(4)
mylist.pop()  # if index not defined it will delete the last element present in list
print(mylist)

#sorting a list  listname.sort()  by default ascending order
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.sort()
print(mylist)

# to sort in decending order
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.sort(reverse =True)
print(mylist)

# Create a copy of the list
course = ["BBA", "BCA", "MCA","B.Com"]
newlist = course.copy()
print(newlist)

# To Join Two Lists
oldcourse = ["BBA", "BCA", "MCA","B.Com"]    # list 1
newcourse = ["MBA","MTech","PHD"]            # list 2
final = oldcourse + newcourse                # list3 = list1+ list2
print(final)

# To Delete the List Completely
course = ["BBA", "BCA", "MCA","B.Com"]
print(course)
del course # delete the list

# To Clear the Elements Present in the List
course = ["BBA", "BCA", "MCA","B.Com"]
print(course)
course. clear ()
print(course)

# Print List Items Using Loop 
course = ["BBA", "BCA", "MCA","B.Com"]
for x in course:
    print(x)
        

   



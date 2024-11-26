# Pandas

# Creating a Series using 
import pandas as pd
a = [5,7,8,9]
mydata = pd.Series(a)
print(mydata)

# Creating series with specific labels
a = [89,94,95,94,87]
sub = pd.Series(a,["DBMS","Java","Linux","Cloud","Python"])
print(sub)

# Creating a Series Using Dictionary

d1 = {"Rouge" : "Guy Crimson","Noir" : "Diablo","Blanc" : "Testarossa","Jaune" : "Carrera",
      "Violet" : "Ultima","Vert" : "Raine","Bleu" : "Miseri"}

ser = pd.Series(d1)
print(ser)


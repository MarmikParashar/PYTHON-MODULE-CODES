# Series Using Pandas

# Creating an Empty Series
import pandas as pd

ser = pd.Series()
print(ser)

# Creating series using numpy array
import numpy as np

info = np.array(['P','a','n','d','a','s'])
s = pd.Series(info)
print(s)

# Creating a series using Scalar
x = pd.Series("P",["Vansh","Saket","Nipun","Kamesh"])
print(x)

# Accessing the Elements of a Series
data = np.array(['C','D','A','C','D','E', 'L','H','I','J','A','S','O','L','A'])
ser1 = pd.Series (data)
print (ser1[2:7])       # for retrieve the elements, slice method used

# Accessing Elements Using Label
data = np.array(['C','D','A','C','D','L','H','I'])
ser = pd.Series(data, index=[1,2,3,4,5,6,7,8])
print (ser[6])


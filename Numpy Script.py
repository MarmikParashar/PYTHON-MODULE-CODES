# Importing Numpy Library
import numpy as np
print(np.__version__)


a = np.array([1,2,3,4])
print(a)
print(type(a))
print(a[2])
print(a[1])

var = np.arange(0,12,2)
print(var)

# O-D Array Creation
zero = np.array(92)
print(zero)
print(type(zero))

# 1-D Array
oneD = np.array([2,4,6,8,9])
print(oneD)

# 2-D Array
twoD = np.array([[2,4,5,6,8,10,12,14],[1,3,5,7,9,11,13,15]])   

''' The no. of elements in the columns should be same 
otherwise it will be inhomogeneous 
and will throw ValueError'''

print(twoD)
print("Array Dimension : " , twoD.ndim)

# 3-D Array
threeD = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(threeD)

# Multi Dimensional Array
arr = np.array([1, 2, 3, 4], ndmin=5)       # ndim method is used for creating multi dimesiona
print(arr)
print('number of dimensions :', arr.ndim)      # array_name.ndim can be used to find the dimensions of your array




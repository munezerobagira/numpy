import numpy as np
# print the version of the numpy
print(np.__version__)
# Creating 1D array with array method 
arr_1= np.array([0,1,2,3,4,5,6,7])
# ndarray type for numpy array
print('Numpy type',type(arr_1))
print('Numpy Array',arr_1)
# print number of dimensions
print('Numpy dimension', arr_1.ndim,'\n')

# Creating 0D array using array method 
arr_2= np.array(45)
print('Numpy Array',arr_2)
print('Numpy dimension',arr_2.ndim,'\n')
# 1D numpy array
arr_3=np.array([24, 56])
print('Numpy Array',arr_3)
print('Numpy dimension',arr_3.ndim,'\n')
# 2D numpy array object 
arr_4=np.array([[1,2,3],[1,3,4]])
print(arr_4)
print(arr_4.ndim)
'''import numpy as np
#lists working

list_a=[1,2,3,4]
list_b=[5,6,7,8]

#print(list_a*list_b)

import numpy as np

numpy_a=np.array([1,2,3,4])
numpy_b=np.array([5,6,7,8])

print(numpy_a)
print(numpy_a*numpy_b)

#common properties
import numpy as np


numpy_array=np.array([1,2,3,4,10.5,"a"])
print(numpy_array.dtype)
print(numpy_array.itemsize)
print((numpy_array.size))

import numpy as np

array_stats = [[1, 2, 3, 8], [4, 5, -6, 0]]

print(np.min(array_stats))
print(np.min(array_stats), axis=0)
print(np.min(array_stats), axis=1)

print(np.max(array_stats))
print(np.max(array_stats,axis=1))

print(np.sum(array_stats,axis=1))
print(np.sum(array_stats,axis=0))
'''
import numpy as np
data_from_text_file = np.genfromtxt('Sample_1.txt', delimiter = ',')
print(data_from_text_file)



#accessing arrays

array_x=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array_x)
print(array_x.size)

print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[:,-3])


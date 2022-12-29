import numpy as np
#array_1D=np.array(([[[1,2,3],[3,4,5]],[[1,2,3],[3,4,5]]]))
array_2D=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))


array_2D=np.array([1,2,3],dtype='int64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)


import numpy as np

numpy_array=np.array([1,2,3,4,5,10.5])
print(numpy_array.dtype)
print(numpy_array.itemsize)



#accessing arrays

array_3D=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(array_3D)
print(array_3D.shape)

three_d=np.zeros(2,3,3)
print(three_d)
import numpy
print(np.full((3,3),5))

print(np.full((2,3),[1,2,3]))

array_r=[1,2,3]
array_repeat=np.repeat(array_r,2,)
print(array_repeat)


array_r=[1,2,3]
array_repeat=np.repeat(array_r,2,axis=0)
print(array_repeat)

array_r=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,2,axis=1)
print(array_repeat)


#math operations

array_math=np.array([1,2,3])

print("Declared array: {}".format(array_math))
print("Add 10 to array: {}".format(array_math+10))
print("sub from  array: {}".format(array_math-10))
print("raise to pow array: {}".format(array_math ** 2))
print("mul array by 5: {}".format(array_math*5))

#algebra with numpy

arr_a=np.ones((2,3))
arr_b=np.full((3,2),2)
print(arr_a)
print(arr_b)

print(arr_a*arr_b)
print(np.matmul(arr_b,arr_a))
import numpy as np

def numpy_function(x,y):
    return 10*x+y

b=np.fromfunction(numpy_function,(4,2),dtype=int)
print(b)
import numpy as np

def numpy_function(x,y,z):
    return 10*x+y+z

b=np.fromfunction(numpy_function,(6,5,6),dtype=int)
print(b)



from numpy import *
import numpy as np
eye(4)
array([
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]

])

dp=np.dtype([('age',int8)])
a= np.array([1,2,3],dtype=dp)
foood=dtype([('name','S20'),('num',int16),('price','f4')])
ao=np.array([('bread',2,23),('milk',19,20)], dtype = foood)
print(ao)
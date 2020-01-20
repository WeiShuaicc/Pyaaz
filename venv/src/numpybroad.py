import numpy as np
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
# print(a + b)


# 迭代
z=np.arange(6).reshape(3,2)
for x in np.nditer(z):
    print(x,end=',')
print('\n')
for x in np.nditer(z,order='C'):
    print(x,end=',')
print('\n')
for x in np.nditer(z.T,order='C'):
    print(x,end=',')
print('\n')
for x in np.nditer(z.T.copy(order='F')):
    print(x,end=',')
print('\n')
for x in np.nditer(z.T.copy(order='C')):
    print(x,end=',')
print('\n')
# 改变迭代的值
az = np.arange(0,72,6)
az = az.reshape(3,4)
print (az)
for x in np.nditer(az,flags=['external_loop'],order='F'):
    print(x,end=',')
print('\n')
# 广播迭代
a = np.arange(0,60,5)
a = a.reshape(3,4)
b = np.array([1,  2,  3,  4])
for x,y in np.nditer([a,b]):
    print ('%d 扩展 %d' % (x,y), end=", " )
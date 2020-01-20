import numpy as np
a=np.arange(36);
# print(a.ndim)
# 调整维度
b=a.reshape(3,4,3)
# print(b.ndim)
aa=np.array([[1,2],[9,8]],dtype=np.complex128)
aa.shape=(4,1)

# 创建空数组 自定义类型
x=np.empty([3,2],dtype=np.int32,order='C')
# print(x)
z=np.zeros((5,),dtype=[('name','i8'),('age','i4')])
# print(z)
xa=[(1,3,4),(2,4,2),(1,4,2,5)]
xs=np.asarray(xa)
# print(xs)
# 实现动态数组 numpy,frombuffer
s=b'Hellow'
zs=np.frombuffer(s,dtype='S3');
# print(zs)

# 使用迭代器创建ndarray
list=range(5)
it=iter(list)
xt=np.fromiter(it,dtype=float)
# print(xt)

# 设置起始值 终止值 步长
xc=np.arange(10,20,2)
# print(xc)

# linspace函数
at=np.linspace(1,10,12,endpoint=True ).reshape([2,6])
# print(at)


# 数组切割  slice
av=np.arange(10);
# aq=slice(5,16,1)
aq=av[2:]
# print(av[aq])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print (a[...,1])   # 第2列元素
# print (a[1,...])   # 第2行元素
# print (a[...,1:])  # 第2列及剩下的所有元素


# 高级索引
xg=np.array([[1,2],[3,4],[5,6]])
# xy=xg[[0,1,0],[0,1,1]]
xy=xg[0:3]
# print(xy)

# 综合运用： ...
az=np.array([[1,2,3],[4,5,6],[7,8,9]])
ab=az[1:3,1:3]
ac=az[1:3,[1,0]]
ad=az[...,1:]



# 过滤· ~
ap=np.array([np.nan,3,12,np.nan])
# print(ap[~np.isnan(ap)])

x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
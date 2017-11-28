# coding=utf-8 
import numpy as np  
from numpy.linalg import cholesky

#mu决定数据点与原点的距离 越小越近
mu = np.array([[0, 0]])
#mu决定形状 协方差矩阵当是单位矩阵的时候就是一个圆形的形状 数值的大小决定了“圆形”半径
Sigma = np.array([[0.1, 0], [0, 0.1]])  
R = cholesky(Sigma)
#1500是采样个数 越大正态的越明显
s = np.dot(np.random.randn(1500, 2), R) + mu  

# 绘图函数，我们的程序不需要
# plt.plot(s[:,0],s[:,1],'+')

#这两个数组分别是那1500个点的横纵坐标 以(0，0)为原点 你可以输出看一下
#print(s[:,0])
#print(s[:,1])


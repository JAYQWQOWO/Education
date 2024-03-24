#胡力谨 202104060625
import numpy as up
#模拟数据
x=np.array([2,3,4,5,6,7])
y=np.array([0,1,2,3,4,5])

#计算拉格朗日插值多项式
def lagrange_interpolation(x,y,xi):
    n=len(x)
    p=np.zeros_like(xi)
    
    for i in range(n):
        L=np.ones_like(xi)
        for j in range(n):
            if j!=i:
                L*=(xi-x[j])/(x[i]-x[j])
        p+=y[i]*L
    
    
    return p
    
#插值结果
xi=np.linspace(0,5,10) #插值点
interpolated_values=lagrange_interpolation(x,y,xi)

print("插值结果：",interpolated_values)

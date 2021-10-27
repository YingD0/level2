import numpy as np 
import matplotlib.pyplot as plt
epslion=-0.99
N=20
gamma=21.7
solve=[]
kk=1
col=['orange','y','forestgreen','royalblue','m','r']
ee=np.math.e
def fun(x):           #被积函数,  x为自变量
    f = np.math.sqrt(round((epslion)-(vx(x)),10)) 
    return f

def T_2n(a, b, n, T_n):       #计算梯形积分
    if n<1:                
        print('n should larger than 1')
    h = (b - a)/n             #步长      
    sum_f = 0.            #初始化，中间变量
    for k in range(0, n):
        sum_f = sum_f + fun(a + (k + 0.5)*h)
    T_2n = T_n/2. + sum_f*h/2.
    return T_2n


def inout(epslion):
    e=epslion
    x1=2**(1/6)-(np.math.log(1-np.math.sqrt(e+1)))/kk
    x2=2**(1/6)-(np.math.log(1+np.math.sqrt(e+1)))/kk
    if (x1>x2):
        x1,x2=x2,x1
    solve.append(x1)
    solve.append(x2)
    return solve[0],solve[1]


def Romberg(a, b, err_min):
    kmax = 6
    tm = np.zeros(kmax,dtype = float)      # 第m行所有的元素
    tm1 = np.zeros(kmax,dtype = float)     #第m+1行所有的元素   
    tm[0] = 0.5*(b-a)*(fun(a) + fun(b))  # 初始值
    #print(tm)
    err = 1.
    k = 0
    np.set_printoptions(precision = 9)
    while(err>err_min and k <kmax-2):  #控制循环次数
        n = 2**k                      # n是区间等分数
        m = 1
        tm1[0] = T_2n(a, b, n, tm[0]) 
        while(err>err_min and m <= (k+1)):  #控制循环次数
            tm1[m] = tm1[m-1]+(tm1[m-1]-(tm[m-1]))/(4.**m-1)
            result = tm1[m]
            err1 = abs(tm1[m]-tm[m-1])
            err2 = abs(tm1[m]-tm1[m-1])
            err = min(err1,err2)
            m = m+1
        tm = np.copy(tm1)
        k = k+1
        #print(tm)     
    return result

#fx=0
def f(n):
    fx=-(n+0.5)*np.math.pi
    fx=fx+Romberg(solve[0], solve[1], 1.e-8)*gamma
    return fx

def vx(x):
    return (1-ee**(-kk*x+kk*2**(1/6)))**2-1

def paint(ii):

    x1=inout(result[ii])
    n1=[vx(x1[0]),vx(x1[1])]
    plt.plot(x1,n1,color=col[i%6])
    solve.clear()

def paint2(i):
    e=result[i]
    x1=2**(1/6)-(np.math.log(1-np.math.sqrt(e+1)))/kk
    x2=2**(1/6)-(np.math.log(1+np.math.sqrt(e+1)))/kk
    xx=np.linspace(x1,x2,10000)
    #p=(result[i]-(np.round(vx(xx))**0.5,4))
    p=(np.abs(result[i]-vx(xx))**0.5)
    plt.plot(xx,-p,color=col[i%6])
    plt.plot(xx,p,color=col[i%6])
    


if __name__=="__main__":
    fig = plt.figure(num=1)
    solve.clear()
    x=np.linspace(0,7,10000)
    v=vx(x)
    plt.ylim(-1,0)
    plt.plot(x,v)
    plt.show()

import numpy as np
from decimal import getcontext
getcontext().prec = 28

def u_need_v(v):
    return ((5 - v)/3)
def v_need_u(u):
    return ((5 - u)/2)

def Jacobi_2():
    p = [0,0]
    while True:
        yield np.array([u_need_v(p[0]),v_need_u(p[1])])
        p = v_need_u(p[1]),u_need_v(p[0]) 

tol = 1e-5
for i , r in enumerate(Jacobi_2()):
    if i > 2 : 
        if np.abs((y - r))[0] < tol or i >= 30 :
            print(i,r)
            break
    print(i,r)
    y = r.copy()
    
```
output results : 

0 [1.66666667 2.5       ]
1 [0.83333333 1.66666667]
2 [1.11111111 2.08333333]
3 [0.97222222 1.94444444]
4 [1.01851852 2.01388889]
5 [0.99537037 1.99074074]
6 [1.00308642 2.00231481]
7 [0.9992284  1.99845679]
8 [1.0005144 2.0003858]
9 [0.9998714 1.9997428]
10 [1.00008573 2.0000643 ]
11 [0.99997857 1.99995713]
12 [1.00001429 2.00001072]
13 [0.99999643 1.99999286]
14 [1.00000238 2.00000179]
```

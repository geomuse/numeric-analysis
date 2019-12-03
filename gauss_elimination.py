# method 1 
def np_gauss_elimin(A,B):
    n = len(B)
    a_b = np.asarray(np.column_stack((A,B)))
    for i in range(0,n-1):
        for k in range(i,n-1):
            lam = a_b[k+1,i] / a_b[i,i]
            print('lam {}'.format(lam))
            a_b[k+1,:] = a_b[k+1,:] -lam * a_b[i,:]
    print(a_b)
    b = a_b[:,-1]
    a = a_b[:,0:-1]


    for k in range(n-1,-1,-1): # back solving
        try : 
            b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
        except ZeroDivisionError as zero : 
            print('det A = 0')
    return b
    print('b = {}'.format(b))
    
# method 2
def gauss_elimin(a,b):
    n = len(b)
    # Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[k,k] != 0.0 :
                lam =a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
                a[i,k] = 0 # 同學們欠 這個步驟 ! 
    print(a)
    for k in range(n-1,-1,-1): # back solving
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
    
# building matrix 
import random as r
import scipy.linalg as sl

def matrix(row,col,rge=range(-5,-1)):
    '''
    row : input the row number you want
    col : input the col number you want 
    rge : range for r.choices 
    '''
    mat = r.choices(rge, k=row*col) # range , length
    x = r.choices(rge,k=row)
    a = np.array(mat).reshape(row,col)
    b = a @ x
    return a , b , x
    
'''
run example

a , b , x = matrix(3,3)
A = np.mat(a.copy())
B = b.copy()
 
np_gaussElimin(A,B)
 
gaussElimin(A , B) 
 
'''
 

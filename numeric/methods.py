import numpy as np
'''
newton method
'''
def newton( xo ,tol , no , f , fx ):
    '''
    xo : initial approximation  
    TOL : tolerance  
    no : maximum number of iterations
    f : function
    fx : derative function
    '''
    i = 0
    while i <= no :
        try:
            f1 = f(xo)
            f2 = fx(xo)
            x = xo - (  f1 / f2 ) 
        except ZeroDivisionError:
#             print('ZeroDivisionError')
            continue
        if np.abs(x-xo) < tol :
            return x
            break 
        i+=1
        xo = x
#         print(xo)
#     if i == no:
    print('maximum number of iterations N0...')

'''
secant method
'''
def secant(po , p1 , tol , no , f ):
    '''
    po , p1 : initial approximations
    TOL : tolerance
    no : maximum number of iterations
    '''
    i = 2 
    qo = f(po)
    q1 = f(p1)
    while i <= no : 
        p = p1 - q1*(p1-po) / (q1 - qo)
        if np.abs(p - p1) < tol :
            return p
            break 
        i+=1
        po , qo , p1 , q1 = p1 , q1 , p , f(p)
    print('The method failed after N0 iterations, N0 =', no)   

'''
bisection method
'''
def bisection( start , end , tol , no , f):
    '''
    start : start points 
    end : end points 
    tol : tolerance 
    no : maximum number of iterations 
    '''
    i = 1 
    st = start
    et = end
    fa = f(st)
    while i <= no:
        p = st + (et-st)/2
        fp = f(p)
        if fp == 0 or (et-st)/2 < tol :
            return p
            break
        i+=1
        if fa * fp > 0 :
             st , fa  = p , fp
        elif fa * fp < 0 : 
            et = p
#     if i == no:
    print('maximum number of iterations N0')

'''
brute-force method
'''
def brute_force(f):
    '''
    rn : round number
    f : func
    '''
    rn = 2
    i = 0
    while True:
        i+= 0.001
        p = np.round(f(i), rn)
        if p == 0 :
            return i
            break


s = ['this is my package']
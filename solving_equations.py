import numpy as np
import pandas as pd
from loguru import logger

logger.add('log/error.log',level='INFO', rotation='10 MB', format='{time:YYYY-MM-DD HH:mm:ss.SSS} | {message}')

class solv_equations:
    def __init__(self) -> None:
        ...

    r'''
    newton method
    '''
    def newton(self, xo ,tol , no , f , fx ):
        r'''
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
                continue
            if np.abs(x-xo) < tol :
                return x
                break 
            i+=1
            xo = x
        return float('nan')

    r'''
    secant method
    '''
    def secant(self,po , p1 , tol , no , f ):
        r'''
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
        return float('nan')   

    r'''
    bisection method
    '''
    def bisection(self, start , end , tol , no , f):
        r'''
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
            i+=1
            if fa * fp > 0 :
                st , fa  = p , fp
            elif fa * fp < 0 : 
                et = p
        return float('nan')

    r'''
    brute-force method
    '''
    def brute_force(self,f):
        r'''
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

class bond_price_estimate :
    def bond_price(self,y,t,c,fv,fre,tp='f'):
        r'''
        t : time 
        fre : frequency
        fv : face value
        y : yield
        c : coupon
        tp : type 
            if type = f :
                function
            else type = fx :
                derative function
        '''
        if tp == 'f' :
            t = t * fre 
            time = np.arange(1,t+1)
            x = (c/fre * fv) / (1 + y/fre) ** time
            return np.sum(x) + fv/((1+y/fre)**t)
        elif tp == 'fx' : 
            t = t * fre 
            time = np.arange(1,t+1)
            x = (-c * fv * time/(fre ** 2) ) / (1 + y/fre) ** (time + 1) 
            return np.sum(x) - fv/(1+y/fre)**(t+1)

    def solve_bond_price_yield(self,t=6.0,c=0.08,fv=1000,fre=1,bp=955.14,tp='f'):
        r'''solve_bond_price_yield.

        t : time 
        c : coupon
        fv : face value
        fre : frequency
        bp : bond price 
        tp : type 
            if type = f :
                function
            else type = fx :
                derative function 
        
        # example 
        
        f = solve_bond_price_yield()
        fx = solve_bond_price_yield(tp='fx')
        nm = solv_equations()
        print('newton : ' + str(nm.newton(0.01,1e-18,500,f,fx)))
        print('bisection : '+str(nm.bisection(-0.8,0.1,1e-16,500,f)))
        print('brute_force : '+str(nm.brute_force(f)))
        print('secant : ' + str(nm.secant(-0.01,0.01,1e-16,500,f)))
        '''
        
        return lambda y : (self.bond_price(y,t,c,fv,fre,tp) - bp)

if __name__ == '__main__':
    bp , nm = bond_price_estimate() , solv_equations()
    f = bp.solve_bond_price_yield()
    fx = bp.solve_bond_price_yield(tp='fx')
    
    print(f'newton : {str(nm.newton(0.01,1e-18,500,f,fx))}.')
    print(f'bisection : {str(nm.bisection(-0.8,0.1,1e-16,500,f))}.')
    print(f'brute_force : {str(nm.brute_force(f))}.')
    print(f'secant : {str(nm.secant(-0.01,0.01,1e-16,500,f))}.')
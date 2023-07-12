import numpy as np
from loguru import logger
from generate_example import bond_price_example , bond_price_example_for_sympy
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))
log = os.path.join(current_dir,'log/error.log')
logger.add(log,level='INFO', rotation='10 MB', format='{time:YYYY-MM-DD HH:mm:ss.SSS} | {message}')

class solv_equations:
    def newton(self, xo ,tol , no , f , fx ):
        for _ in range(no):
            try:
                f1 = f(xo)
                f2 = fx(xo)
                x = xo - (  f1 / f2 ) 
            except ZeroDivisionError:
                continue
            if np.abs(x-xo) < tol :
                return x
            xo = x
        return None

    def secant(self,po , p1 , tol , no , f ):
        qo = f(po)
        q1 = f(p1)
        for _ in range(no):
            p = p1 - q1*(p1-po) / (q1 - qo)
            if abs(p - p1) < tol :
                return p
            po , qo , p1 , q1 = p1 , q1 , p , f(p)
        return None   

    def secant_variants(self,po,p1,tol,no,f):
        fcl = 0
        for _ in range(no):
            fo = f(po)
            f1 = f(p1)
            c = (p1*fo - po*f1) / (fo - f1)
            fc = f(c)
            if fc == 0 or abs(fc - fcl)< tol:
                return c
            if fo * fc < 0 :
                b = c
            else :
                a = c
            fcl = fc
        return None
            
    def bisection(self, start , end , tol , no , f):
        st = start
        et = end
        fa = f(st)
        for _ in range(no):
            p = st + (et-st)/2
            fp = f(p)
            if fp == 0 or (et-st)/2 < tol :
                return p
            if fa * fp > 0 :
                st , fa  = p , fp
            elif fa * fp < 0 : 
                et = p
        return None
        
    def brute_force(self,rn,no,f):
        i = 0
        for _ in range(no):
            i+=0.001
            p = round(f(i),rn)
            if p == 0 : 
                return i
        return None

    def fixed_point(self,xo,no,f):
        x1 = xo
        for _ in range(no):
            ...

if __name__ == '__main__':
    bp , bpe ,  nm = bond_price_example_for_sympy() , bond_price_example() , solv_equations()
    t , c , fv , fre = 0.25 , 0 , 100 , 0.25
    f = bp.solve_bond_price_yield(t,c,fv,fre,bp=99.6)

    # print(f'newton : {nm.newton(0.01,1e-18,500,f,fx)}.')
    print(f'secant : {nm.secant(-0.01,0.01,1e-16,500,f)}.')
    print(f'secant variants : {nm.secant_variants(-0.01,0.01,1e-16,500,f)}.')
    print(f'bisection : {nm.bisection(-0.8,0.1,1e-16,500,f)}.')
    print(f'brute_force : {nm.brute_force(2,500,f)}.')
    
    b = bp.bond_price(nm.secant(-0.01,0.01,1e-16,500,f),t,c,fv,fre,1)
    print(b)

    b = bp.bond_price(1.6064/100,t,c,fv,fre,1)
    print(b)
   
    x = bpe.bond_price(0.01,0.25,0.05,100,0.25,'fx')
    y = bp.bond_price_differential(0.01,0.25,0.05,100,0.25)
    print(x,y)
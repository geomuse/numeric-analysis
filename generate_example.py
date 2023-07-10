import numpy as np
import sympy as sy

class bond_price_example :
    def bond_price(self,y,t,c,fv,fre,tp='f'):
        if tp == 'f' :
            t = t * fre 
            time = np.arange(1,t+1)
            x = (c/fre * fv) / (1 + y/fre) ** time
            return sum(x) + fv/((1+y/fre)**t)
        elif tp == 'fx' : 
            t = t * fre 
            time = np.arange(1,t+1)
            x = (-c * fv * time/(fre ** 2) ) / (1 + y/fre) ** (time + 1) 
            return sum(x) - fv/(1+y/fre)**(t+1)

    def solve_bond_price_yield(self,t=6.0,c=0.08,fv=1000,fre=1,bp=955.14,tp='f'):
        return lambda y : (self.bond_price(y,t,c,fv,fre,tp) - bp)

class bond_price_example_sympy :
    def bond_price(self,y,t,c,fv,fre):
        time = np.arange(fre,t+fre,fre)
        x = (c/fre * fv) / (1 + y/fre) ** time
        print(x)
        return np.sum(x) + fv/((1+y/fre)**time[-1])
        # return np.sum(x) + fv/((1+y/fre)**time)
    
    def bond_price_exp(self,y,t,c,fv,fre):
        t = t * fre 
        time = np.arange(1,t+1)
        x = (c/fre * fv) * np.exp()
        print(x)

    def bond_price_differential(self,y,t,c,fv,fre):
        time = t * fre 
        x = (-c * fv * time/(fre ** 2) ) / (1 + y/fre) ** (time + 1) 
        return sum(x) - fv/(1+y/fre)**(t+1)

    def solve_bond_price_yield(self,t=6.0,c=0.08,fv=1000,fre=1,bp=955.14,tp='f'):
        return lambda y : (self.bond_price(y,t,c,fv,fre,tp) - bp)
    
    '''
    time 有问题. [done]
    应该是按照付息次数跑.
    计算有问题. [loading.]
    '''

if __name__ == '__main__':
    bp = bond_price_example_sympy()
    y = np.array([1.6064,2.0202,2.2495,2.2949,2.4238])/100
    t = np.array([0.25,0.5,1.0,1.5,2.0])
    c = np.array([0.0,0.0,0.0,4.0,5.0])/100
    fv = np.array([100]*5)
    fre = np.array([0.25,0.5,1,0.5,0.5])
    bond_price = [ bp.bond_price(yi,ti,ci,fvi,frei) for yi , ti , ci , fvi , frei in zip(y,t,c,fv,fre)]
    # bond_price = bp.bond_price_exp(y,t,c,fv,fre)
    print(bond_price)
    
    bpe = bond_price_example()
    bond_price = bpe.bond_price(y[0],t[0],c[0],fv[0],fre[0],tp='f')
    print(bond_price)
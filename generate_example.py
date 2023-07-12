import numpy as np

class bond_price_example :
    def bond_price(self,y,t,c,fv,fre,tp='f'):
        if tp == 'f' :
            t = t * fre 
            time = np.arange(1,t+1)
            x = (c/fre * fv) / (1 + y*fre) ** time
            return sum(x) + fv/((1+y*fre)**t)
        
        elif tp == 'fx' : 
            t = t * fre 
            time = np.arange(1,t+1)
            x = (-c * fv * time/(fre ** 2) ) / (1 + y/fre) ** (time + 1) 
            return sum(x) - fv/(1+y/fre)**(t+1)

    def solve_bond_price_yield(self,t=6.0,c=0.08,fv=1000,fre=1,bp=955.14,tp='f'):
        return lambda y : (self.bond_price(y,t,c,fv,fre,tp) - bp)

class bond_price_example_for_sympy :
    def bond_price(self,y,t,c,fv,fre=None,met=1):
        time = np.arange(fre,t+fre,fre)
        method = {
            1 : self._fixed_bonds(y,time,c,fv,fre) , 
            2 : self._exponential(y,time,c,fv) , 
        }
        bond_price = method.get(met)
        return bond_price
    
    def _exponential(self,y,time,c,fv):
        coupon = c*fv
        x = coupon * np.exp(-y*time)
        bond_price = sum(x) + fv * np.exp(-y*time[-1])
        return bond_price

    def _fixed_bonds(self,y,time,c,fv,fre):
        coupon = (c*fre*fv)
        x = coupon / (1 + y*fre) ** time
        bond_price = sum(x) + fv / ((1+y*fre)**time[-1])
        return bond_price

    def bond_price_differential(self,y,t,c,fv,fre):
        ...
        #有没有好用的套件可以处理?除了symsy.

    def solve_bond_price_yield(self,t,c,fv,fre=None,met=1,bp=105):
        return lambda y : self.bond_price(y,t,c,fv,fre,met) - bp

class bootstrap:
    def exponential(self,coupon,z,time,bond_price):
        x = coupon * np.exp(-z*time)
        x = x[~np.isnan(x)]
        x = bond_price - sum(x)
        r = -np.log(x/coupon[-1])/time[-1]

if __name__ == '__main__':
    # estimate bond price.
    bp = bond_price_example_for_sympy()
    y = np.array([1.6064,2.0202,2.2495,2.2949,2.4238])/100
    z = np.array([1.603,2.010,2.225,2.284,2.416])/100
    t = np.array([0.25,0.5,1.0,1.5,2.0])
    c = np.array([0.0,0.0,0.0,4.0,5.0])/100
    fv = np.array([100]*5)
    fre = np.array([0.25,0.5,1,0.5,0.5])
    bond_price = [ bp.bond_price(yi,ti,ci,fvi,frei) for yi , ti , ci , fvi , frei in zip(y,t,c,fv,fre)]
    # print(bond_price)

    bond_price = [ bp.bond_price(yi,ti,ci,fvi,frei,1) for yi , ti , ci , fvi , frei in zip(y,t,c,fv,fre)]
    # print(bond_price)

    # bootstrap.
    coupon = np.array([2,2,102])
    z = np.array([0.02010,0.02225,np.nan])
    time = np.array([0.5,1.0,1.5])
    bond_price = 102.5
    bs = bootstrap()
    bs.exponential(coupon,z,time,bond_price)
    
    bpe = bond_price_example()
    bond_price = [ bpe.bond_price(yi,ti,ci,fvi,frei,tp='f') for yi , ti , ci , fvi , frei in zip(y,t,c,fv,fre)]
    # print(bond_price)

    bp = bond_price_example_for_sympy()
    
    y = 0.06
    fv = 2000
    coupon = 0.08
    time = 5
    fre = 1

    b = bp.bond_price(y,time,coupon,fv,fre,1)
    print(b)
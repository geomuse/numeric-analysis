'''
bond price method 
'''

def w(y,t,c,fv,fre,tp):
    '''
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
    try :
        if tp == 'f' :
            t = t * fre 
            time = np.arange(1,t+1)
            x = (c/fre * fv) / (1 + y/fre) ** time
            return np.sum(x) + fv/(1+y/fre)**time[-1]
        elif tp == 'fx' : 
            t = t * fre 
            time = np.arange(1,t+1)
            x = (-c * fv * time/(fre ** 2) ) / (1 + y/fre) ** (time + 1) 
            return np.sum(x) - fv/(1+y/fre)**(time[-1]+1)
    except : 
        print('method wrong') 
        
def solve_bond_price_yield(t=6.0,c=0.08,fv=1000,fre=1,bp=955.14,tp='f'):
    '''
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
    
    example 
    
    f = solve_bond_price_yield()
    fx = solve_bond_price_yield(tp='fx')
    f = solve_bond_price_yield(fre=1)
    print('newton : ' + str(nm.newton(0.01,1e-18,500,f,fx)))
    print('bisection : '+str(nm.bisection(-0.8,0.1,1e-16,500,f)))
    print('brute_force ：'+str(nm.brute_force(f)))
    print('secant : ' + str(nm.secant(-0.01,0.01,1e-16,500,f)))
    '''
    
    return lambda y : (w(y,t,c,fv,fre,tp) - bp)
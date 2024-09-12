# solving problems.

## bond_price.

```
y : yield
t : time 
c : coupon
fv : face value
fre : frequency
tp : type 
    if type = f :
        function
    else type = fx :
        derative function
```

## solve_bond_price_yield.

```
y : yield
t : time 
c : coupon
fv : face value
fre : frequency
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
```
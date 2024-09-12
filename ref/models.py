class numeric_analysis:

    def bisection(self,f, a, b, tol=1e-6):
        if f(a) * f(b) > 0:
            raise ValueError("The function must have opposite signs at a and b")
        
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            yield midpoint  # 每次迭代返回中间值
            if f(midpoint) == 0:
                break
            elif f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        yield (a + b) / 2.0
    
    def newton(self,f, df, x0, tol=1e-6, max_iter=100):
        x = x0
        for _ in range(max_iter):
            fx = f(x)
            yield x  # 每次迭代返回当前估计值
            if abs(fx) < tol:
                break
            dfx = df(x)
            if dfx == 0:
                raise ValueError("Derivative is zero. No solution found.")
            x = x - fx / dfx

    def secant(self,f, x0, x1, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            fx0 = f(x0)
            fx1 = f(x1)
            yield x1  # 每次迭代返回当前估计值
            if abs(fx1) < tol:
                break
            denominator = (fx1 - fx0)
            if denominator == 0:
                raise ValueError("Zero denominator. No solution found.")
            x2 = x1 - fx1 * (x1 - x0) / denominator
            x0, x1 = x1, x2
    
    def false_position(self,f, a, b, tol=1e-6, max_iter=100):
        if f(a) * f(b) > 0:
            raise ValueError("The function must have opposite signs at a and b")

        for _ in range(max_iter):
            fa = f(a)
            fb = f(b)
            x = b - fb * (b - a) / (fb - fa)
            yield x  # 每次迭代返回当前估计值
            fx = f(x)
            if abs(fx) < tol:
                break
            elif fa * fx < 0:
                b = x
            else:
                a = x

    def fixed_point(self,g, x0, tol=1e-6, max_iter=100):
        x = x0
        for _ in range(max_iter):
            x_new = g(x)
            yield x_new  # 每次迭代返回当前估计值
            if abs(x_new - x) < tol:
                break
            x = x_new

nm = numeric_analysis()

f = lambda x: x**3 - x - 2
for root in nm.bisection(f, 1, 2):
    print(f"Bisection Step Root Approximation: {root}")
print('\n')
df = lambda x: 3*x**2 - 1
for root in nm.newton(f, df, 1.5):
    print(f"Newton's Step Root Approximation: {root}")
print('\n')
for root in nm.secant(f, 1, 2):
    print(f"Secant Step Root Approximation: {root}")
print('\n')
# Example usage:
f = lambda x: x**3 - x - 2
for root in nm.false_position(f, 1, 2):
    print(f"False Position Step Root Approximation: {root}")
print('\n')
# Example usage:
g = lambda x: (x + 2)**(1/3)
for root in nm.fixed_point(g, 1.5):
    print(f"Fixed-Point Iteration Step Root Approximation: {root}")
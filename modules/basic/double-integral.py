import sympy as sp

x, y = sp.symbols('x y')
f = x*y

I = sp.integrate(sp.integrate(f, (x, 0, 2)), (y, 0, 3))
print("Double Integral:", I)

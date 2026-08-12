import sympy as sp

x = sp.Symbol('x')
f = sp.exp(x) * sp.sin(x)

I = sp.integrate(f, (x, 0, sp.pi))
print("Integral:", I)

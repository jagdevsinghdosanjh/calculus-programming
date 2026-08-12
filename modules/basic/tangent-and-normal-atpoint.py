import sympy as sp

x = sp.Symbol('x')
f = x**3 - 3*x + 2

a = 1  # point of contact
slope = sp.diff(f, x).subs(x, a)
tangent = slope*(x - a) + f.subs(x, a)

print("Slope =", slope)
print("Tangent equation =", tangent)

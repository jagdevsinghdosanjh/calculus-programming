import sympy as sp

x = sp.Symbol('x')
f = sp.Piecewise((x**2, x < 1), (2*x - 1, x >= 1))

print("Left limit =", sp.limit(f, x, 1, dir='-'))
print("Right limit =", sp.limit(f, x, 1, dir='+'))
print("Value at 1 =", f.subs(x, 1))

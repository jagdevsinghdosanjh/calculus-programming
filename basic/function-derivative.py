import sympy as sp

x = sp.Symbol('x')
f = x**3 + 5*x**2 - 7*x + 10

df = sp.diff(f, x)
print("Function:", f)
print("Derivative:", df)

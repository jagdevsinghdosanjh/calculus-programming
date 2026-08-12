import sympy as sp

x = sp.Symbol('x')
f = x**3 - 6*x**2 + 9*x + 1

df = sp.diff(f, x)
critical_points = sp.solve(df, x)

print("Critical points =", critical_points)
for cp in critical_points:
    print(cp, "Second derivative =", sp.diff(f, x, 2).subs(x, cp))

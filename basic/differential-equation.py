import sympy as sp

x = sp.Symbol('x')
y = sp.Function('y')

ode = sp.Eq(sp.diff(y(x), x), y(x))
sol = sp.dsolve(ode)
print(sol)

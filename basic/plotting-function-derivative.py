import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.Symbol('x')
f = sp.sin(x) * sp.exp(x)
df = sp.diff(f, x)

f_l = sp.lambdify(x, f, 'numpy')
df_l = sp.lambdify(x, df, 'numpy')

X = np.linspace(-2, 2, 400)
plt.plot(X, f_l(X), label="f(x)")
plt.plot(X, df_l(X), label="f'(x)")
plt.legend()
plt.grid()
plt.show()

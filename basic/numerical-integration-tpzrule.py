import numpy as np

def f(x):
    return np.sqrt(1 + x**2)

def trapezoidal(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return h * (y[0]/2 + y[-1]/2 + y[1:-1].sum())

print(trapezoidal(0, 2, 1000))

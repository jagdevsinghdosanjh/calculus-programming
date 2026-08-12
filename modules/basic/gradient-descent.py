import numpy as np

def f(x):
    return x**2 + 5*x + 6

def df(x):
    return 2*x + 5

x = 10
lr = 0.1

for i in range(20):
    x -= lr * df(x)
    print(i, x)

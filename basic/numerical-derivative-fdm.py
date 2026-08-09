def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)

import math
print(derivative(lambda x: math.sin(x), 1.0))

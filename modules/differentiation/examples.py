# modules/differentiation/examples.py

import random

def random_polynomial():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    return f"{a}*x**3 + {b}*x**2 + {c}*x"

def random_trig():
    funcs = ["sin", "cos", "tan"]
    func = random.choice(funcs)
    k = random.randint(1, 5)
    return f"{func}({k}*x)"

def random_exp_log():
    k = random.randint(1, 5)
    return random.choice([f"exp({k}*x)", f"log({k}*x)"])

def random_product():
    return f"({random_polynomial()})*({random_trig()})"

def random_chain():
    return f"sin({random_polynomial()})"

def generate_jee_derivative():
    """
    Returns a random JEE-style derivative question.
    """

    types = [
        random_polynomial,
        random_trig,
        random_exp_log,
        random_product,
        random_chain,
    ]

    generator = random.choice(types)
    return generator()

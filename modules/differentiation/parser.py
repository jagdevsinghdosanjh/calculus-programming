# modules/differentiation/parser.py

import sympy as sp

# Allowed functions
FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "log": sp.log,
    "exp": sp.exp,
    "sqrt": sp.sqrt,
}

def parse_expression(expr_str: str):
    """
    Converts user input string into a SymPy expression.
    Handles implicit multiplication and common math functions.
    """

    # Replace ^ with ** for power
    expr_str = expr_str.replace("^", "**")

    # Replace common functions (Ruff SIM118 fix: no .keys())
    for name in FUNCTIONS:
        expr_str = expr_str.replace(name, name)

    try:
        expr = sp.sympify(expr_str, locals=FUNCTIONS)
        return expr
    except (sp.SympifyError, TypeError, ValueError):
        return None


# # modules/differentiation/parser.py

# import sympy as sp

# # Allowed functions
# FUNCTIONS = {
#     "sin": sp.sin,
#     "cos": sp.cos,
#     "tan": sp.tan,
#     "log": sp.log,
#     "exp": sp.exp,
#     "sqrt": sp.sqrt
# }

# def parse_expression(expr_str: str):
#     """
#     Converts user input string into a SymPy expression.
#     Handles implicit multiplication and common math functions.
#     """

#     # Replace ^ with ** for power
#     expr_str = expr_str.replace("^", "**")

#     # Replace common functions
#     for name, func in FUNCTIONS.items():
#         expr_str = expr_str.replace(name, f"{name}")

#     try:
#         x = sp.Symbol('x')
#         expr = sp.sympify(expr_str, locals=FUNCTIONS)
#         return expr
#     except Exception:
#         return None

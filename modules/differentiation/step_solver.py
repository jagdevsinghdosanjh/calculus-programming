# modules/differentiation/step_solver.py

import sympy as sp
from .parser import parse_expression
from .rules import identify_rule
from .formatter import format_steps

def derivative_steps(expr_str: str):
    """
    Main step-by-step derivative solver.
    Returns: steps_text, steps_latex, final_answer
    """

    expr = parse_expression(expr_str)
    if expr is None:
        return "Invalid expression", "", ""

    x = sp.Symbol('x')
    steps = []

    # Step 1: Identify rule
    rule = identify_rule(expr)
    steps.append({
        "text": f"Identified rule: {rule}",
        "expr": expr
    })

    # Step 2: Differentiate
    derivative_expr = sp.diff(expr, x)
    steps.append({
        "text": "Differentiate the expression",
        "expr": derivative_expr
    })

    # Step 3: Simplify
    simplified = sp.simplify(derivative_expr)
    steps.append({
        "text": "Simplify the derivative",
        "expr": simplified
    })

    # Format output
    steps_text, steps_latex = format_steps(steps)

    return steps_text, steps_latex, simplified

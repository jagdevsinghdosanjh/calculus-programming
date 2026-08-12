# modules/differentiation/formatter.py

import sympy as sp

def format_steps(steps):
    """
    Converts step list into clean text + LaTeX.
    """
    text_output = ""
    latex_output = ""

    for i, step in enumerate(steps, 1):
        text_output += f"Step {i}: {step['text']}\n"
        latex_output += f"Step {i}: ${sp.latex(step['expr'])}$\n\n"

    return text_output, latex_output

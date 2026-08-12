# modules/differentiation/tangent_explorer.py

import sympy as sp
import numpy as np
import plotly.graph_objects as go

def compute_tangent(expr_str: str, a_value: float):
    """
    Computes f(x), f'(x), and tangent line at x = a.
    Returns: (expr, derivative, tangent_expr, a_value, f(a), f'(a))
    """

    x = sp.Symbol("x")

    try:
        expr = sp.sympify(expr_str)
    except (sp.SympifyError, TypeError, ValueError):
        return None, None, None, None, None, None

    derivative = sp.diff(expr, x)

    # Evaluate f(a) and f'(a)
    f_a = float(expr.subs(x, a_value))
    fp_a = float(derivative.subs(x, a_value))

    # Tangent line: y = f(a) + f'(a)(x - a)
    tangent_expr = f_a + fp_a * (x - a_value)

    return expr, derivative, tangent_expr, a_value, f_a, fp_a


def plot_tangent(expr, tangent_expr, a_value):
    """
    Creates a Plotly graph of f(x) and tangent line at x = a.
    """

    x = sp.Symbol("x")

    # Generate numerical values
    xs = np.linspace(a_value - 5, a_value + 5, 400)
    f_vals = [float(expr.subs(x, val)) for val in xs]
    t_vals = [float(tangent_expr.subs(x, val)) for val in xs]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=xs,
        y=f_vals,
        mode="lines",
        name="f(x)",
        line=dict(color="blue")
    ))

    fig.add_trace(go.Scatter(
        x=xs,
        y=t_vals,
        mode="lines",
        name="Tangent Line",
        line=dict(color="red", dash="dash")
    ))

    fig.add_trace(go.Scatter(
        x=[a_value],
        y=[float(expr.subs(x, a_value))],
        mode="markers",
        name="Point of Tangency",
        marker=dict(color="green", size=10)
    ))

    fig.update_layout(
        title="Function & Tangent Line",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white"
    )

    return fig

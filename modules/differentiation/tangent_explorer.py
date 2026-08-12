# modules/differentiation/tangent_explorer.py

import numpy as np
import plotly.graph_objects as go
import sympy as sp


def compute_tangent(expr_str: str, a_value: float):
    """
    Computes f(x), f'(x), and tangent line at x = a.
    """

    x = sp.Symbol("x")

    try:
        expr = sp.sympify(expr_str)
    except (sp.SympifyError, TypeError, ValueError):
        return None, None, None, None, None, None

    # Compute derivative and simplify to avoid ArrayDerivative
    derivative = sp.simplify(sp.diff(expr, x))

    # Safe numeric evaluation
    try:
        f_a = float(sp.N(expr.subs(x, a_value)))
        fp_a = float(sp.N(derivative.subs(x, a_value)))
    except (TypeError, ValueError):
        return None, None, None, None, None, None

    # Tangent line as pure numeric lambda (no Symbol - float)
    def tangent_func(val: float) -> float:
        return f_a + fp_a * (val - a_value)

    return expr, derivative, tangent_func, a_value, f_a, fp_a


def plot_tangent(expr, tangent_func, a_value: float):
    """
    Creates a Plotly graph of f(x) and tangent line at x = a.
    """

    x = sp.Symbol("x")

    xs = np.linspace(a_value - 5.0, a_value + 5.0, 400)

    f_vals = []
    t_vals = []

    for val in xs:
        try:
            f_vals.append(float(sp.N(expr.subs(x, val))))
            t_vals.append(float(tangent_func(val)))
        except (TypeError, ValueError):
            f_vals.append(np.nan)
            t_vals.append(np.nan)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=xs,
            y=f_vals,
            mode="lines",
            name="f(x)",
            line={"color": "blue"},
        )
    )

    fig.add_trace(
        go.Scatter(
            x=xs,
            y=t_vals,
            mode="lines",
            name="Tangent Line",
            line={"color": "red", "dash": "dash"},
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[a_value],
            y=[float(sp.N(expr.subs(x, a_value)))],
            mode="markers",
            name="Point of Tangency",
            marker={"color": "green", "size": 10},
        )
    )

    fig.update_layout(
        title="Function & Tangent Line",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
    )

    return fig

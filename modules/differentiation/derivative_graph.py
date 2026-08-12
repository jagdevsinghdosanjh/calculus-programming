import numpy as np
import plotly.graph_objects as go
import sympy as sp


def plot_derivative(expr_str: str):
    """
    Plots f(x) and f'(x) using numeric evaluation.
    """

    x = sp.Symbol("x")

    try:
        expr = sp.sympify(expr_str)
    except (sp.SympifyError, TypeError, ValueError):
        return None

    derivative = sp.simplify(sp.diff(expr, x))

    xs = np.linspace(-5.0, 5.0, 400)
    f_vals = []
    fp_vals = []

    for val in xs:
        try:
            f_vals.append(float(sp.N(expr.subs(x, val))))
            fp_vals.append(float(sp.N(derivative.subs(x, val))))
        except (TypeError, ValueError):
            f_vals.append(np.nan)
            fp_vals.append(np.nan)

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
            y=fp_vals,
            mode="lines",
            name="f'(x)",
            line={"color": "red"},
        )
    )

    fig.update_layout(
        title="Function and Derivative",
        xaxis_title="x",
        yaxis_title="y",
        template="plotly_white",
    )

    return fig

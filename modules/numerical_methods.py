import streamlit as st
import numpy as np
import sympy as sp

def run_numerical():
    # Numerical Derivative
    st.subheader("Numerical Derivative")
    expr_input = st.text_input("Enter function:", "sin(x)")
    point = st.number_input("Point:", value=1.0)
    h = st.number_input("Step size h:", value=1e-5)

    try:
        x = sp.Symbol("x")
        expr = sp.sympify(expr_input)
        f = sp.lambdify(x, expr, "numpy")

        derivative = (f(point + h) - f(point - h)) / (2 * h)
        st.success(f"Numerical derivative ≈ {derivative}")

    except (sp.SympifyError, TypeError, ValueError) as e:
        st.error(f"Error: {e}")

    # Numerical Integration
    st.subheader("Numerical Integration (Trapezoidal)")
    expr_input2 = st.text_input("Integrand:", "cos(x)")
    a = st.number_input("Lower limit:", value=0.0)
    b = st.number_input("Upper limit:", value=3.14)
    n = st.number_input("Number of intervals:", value=1000)

    try:
        x = sp.Symbol("x")
        expr2 = sp.sympify(expr_input2)
        f2 = sp.lambdify(x, expr2, "numpy")

        xs = np.linspace(a, b, int(n) + 1)
        ys = f2(xs)
        h2 = (b - a) / n
        trap = h2 * (ys[0] / 2 + ys[-1] / 2 + ys[1:-1].sum())

        st.success(f"Trapezoidal Integral ≈ {trap}")

    except (sp.SympifyError, TypeError, ValueError) as e:
        st.error(f"Error: {e}")
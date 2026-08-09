# modules/derivatives.py
import streamlit as st
import sympy as sp

def run_derivatives():
    st.header("Derivative Calculator")

    x = sp.Symbol('x')
    expr_input = st.text_input("Enter function f(x):", "x**3 + 5*x")

    try:
        expr = sp.sympify(expr_input)
        derivative = sp.diff(expr, x)
        st.success(f"f'(x) = {derivative}")
    except Exception as e:
        st.error(f"Error: {e}")

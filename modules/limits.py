# modules/limits.py
import streamlit as st
import sympy as sp

def run_limits():
    st.header("Limits Calculator")

    x = sp.Symbol('x')
    expr_input = st.text_input("Enter expression (use x):", "sin(x)/x")
    point = st.number_input("Limit point:", value=0.0)

    try:
        expr = sp.sympify(expr_input)
        limit_value = sp.limit(expr, x, point)
        st.success(f"Limit as x → {point} = {limit_value}")
    except Exception as e:
        st.error(f"Error: {e}")

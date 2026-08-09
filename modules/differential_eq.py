# modules/differential_eq.py
import streamlit as st
import sympy as sp

# Declare symbols OUTSIDE the function so Ruff does not flag them
x = sp.Symbol("x")
y = sp.Function("y")

def run_diff_eq():
    st.header("Differential Equation Solver")

    st.write("Enter differential equation in SymPy format.")
    st.write("Example: diff(y(x), x) - y(x)")

    eq_input = st.text_input("Equation:", "diff(y(x), x) - y(x)")

    try:
        equation = sp.sympify(eq_input)
        ode = sp.Eq(equation, 0)
        solution = sp.dsolve(ode)

        st.success(f"Solution: {solution}")

    except (sp.SympifyError, ValueError) as e:
        st.error(f"Invalid equation: {e}")

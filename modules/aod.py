import streamlit as st
import sympy as sp

def run_aod():
    st.header("Applications of Derivatives")

    x = sp.Symbol("x")
    expr_input = st.text_input("Enter function:", "x**3 - 6*x**2 + 9*x + 1")

    try:
        expr = sp.sympify(expr_input)
        derivative = sp.diff(expr, x)
        second_derivative = sp.diff(expr, x, 2)

        st.subheader("Critical Points")
        critical_points = sp.solve(derivative, x)
        st.write(critical_points)

        st.subheader("Maxima / Minima Classification")
        for cp in critical_points:
            sd = second_derivative.subs(x, cp)

            # Numeric evaluation using SymPy's N()
            sd_numeric = sp.N(sd)

            # If numeric evaluation fails, skip classification
            if not sd_numeric.is_real:
                st.info(f"x = {cp} → Cannot classify (symbolic expression)")
                continue

            if sd_numeric > 0:
                st.success(f"x = {cp} → Local Minimum")
            elif sd_numeric < 0:
                st.warning(f"x = {cp} → Local Maximum")
            else:
                st.info(f"x = {cp} → Point of Inflection")

    except (sp.SympifyError, ValueError) as e:
        st.error(f"Invalid expression: {e}")

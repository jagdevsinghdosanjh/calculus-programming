# modules/derivatives.py

import streamlit as st
from modules.differentiation.step_solver import derivative_steps

def run_derivatives():
    st.header("Derivative Calculator (Step-by-Step)")

    expr_input = st.text_input("Enter function f(x):", "x**3 + 5*x")

    if st.button("Solve Derivative"):
        steps_text, steps_latex, final_answer = derivative_steps(expr_input)

        st.subheader("🧩 Step-by-Step Explanation")
        st.text(steps_text)

        st.subheader("📐 LaTeX Steps")
        st.markdown(steps_latex)

        st.subheader("✅ Final Answer")
        st.latex(final_answer)

# # modules/derivatives.py
# import streamlit as st
# import sympy as sp

# def run_derivatives():
#     st.header("Derivative Calculator")

#     x = sp.Symbol('x')
#     expr_input = st.text_input("Enter function f(x):", "x**3 + 5*x")

#     try:
#         expr = sp.sympify(expr_input)
#         derivative = sp.diff(expr, x)
#         st.success(f"f'(x) = {derivative}")
#     except Exception as e:
#         st.error(f"Error: {e}")

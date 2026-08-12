# modules/derivatives.py

import streamlit as st
from modules.differentiation.step_solver import derivative_steps
from modules.differentiation.tangent_explorer import compute_tangent, plot_tangent
from modules.differentiation.derivative_graph import plot_derivative


def run_derivatives():
    st.header("Derivative Calculator (Step-by-Step)")

    expr_input = st.text_input("Enter function f(x):", "x**3 + 5*x")

    # -------------------------------
    # Step-by-step derivative solver
    # -------------------------------
    if st.button("Solve Derivative"):
        steps_text, steps_latex, final_answer = derivative_steps(expr_input)

        st.subheader("🧩 Step-by-Step Explanation")
        st.text(steps_text)

        st.subheader("📐 LaTeX Steps")
        st.markdown(steps_latex)

        st.subheader("✅ Final Answer")
        st.latex(final_answer)

    # -------------------------------
    # Tangent Line Explorer
    # -------------------------------
    st.markdown("---")
    st.subheader("📈 Tangent Line Explorer")

    col1, _ = st.columns([1, 1])
    with col1:
        a_value = st.number_input("Point of tangency (a):", value=1.0)

    if st.button("Show Tangent Line"):
        expr, _, tangent_func, a_val, f_a, fp_a = compute_tangent(expr_input, a_value)

        # Guard for Pylance: ensure no None is passed
        if expr is None or tangent_func is None or a_val is None:
            st.error("Invalid expression. Please enter a valid function.")
        else:
            st.markdown(f"**f({a_val}) = {f_a}**")
            st.markdown(f"**f'({a_val}) = {fp_a}**")

            fig = plot_tangent(expr, tangent_func, float(a_val))
            st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # Derivative Graph f'(x)
    # -------------------------------
    st.markdown("---")
    st.subheader("📉 Derivative Graph f'(x)")

    if st.button("Show Derivative Graph"):
        fig = plot_derivative(expr_input)

        if fig is None:
            st.error("Invalid expression. Please enter a valid function.")
        else:
            st.plotly_chart(fig, use_container_width=True)

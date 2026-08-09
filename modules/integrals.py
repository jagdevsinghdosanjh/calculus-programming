# modules/integrals.py
# modules/integrals.py
import streamlit as st
import sympy as sp

def run_integrals():
    st.header("Integration Engine")

    x = sp.Symbol("x")
    expr_input = st.text_input("Enter integrand:", "sin(x)*exp(x)")

    mode = st.radio("Select type:", ["Indefinite", "Definite"])

    try:
        expr = sp.sympify(expr_input)

        if mode == "Indefinite":
            result = sp.integrate(expr, x)
            st.success(f"∫ f(x) dx = {result}")

        else:
            a = st.number_input("Lower limit:", value=0.0)
            b = st.number_input("Upper limit:", value=3.14)
            result = sp.integrate(expr, (x, a, b))
            st.success(f"∫ from {a} to {b} = {result}")

    except (sp.SympifyError, ValueError) as e:
        st.error(f"Invalid integrand: {e}")

# import streamlit as st
# import sympy as sp

# def run_integrals():
#     st.header("Integration Engine")

#     x = sp.Symbol('x')
#     expr_input = st.text_input("Enter integrand:", "sin(x)*exp(x)")

#     mode = st.radio("Select type:", ["Indefinite", "Definite"])

#     try:
#         expr = sp.sympify(expr_input)

#         if mode == "Indefinite":
#             result = sp.integrate(expr, x)
#             st.success(f"∫ f(x) dx = {result}")

#         else:
#             a = st.number_input("Lower limit:", value=0.0)
#             b = st.number_input("Upper limit:", value=3.14)
#             result = sp.integrate(expr, (x, a, b))
#             st.success(f"∫ from {a} to {b} = {result}")

#     except Exception as e:
#         st.error(f"Error: {e}")

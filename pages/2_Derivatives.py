# pages/2_Derivatives.py

import streamlit as st
from modules.derivatives import run_derivatives

st.set_page_config(page_title="Derivatives", layout="wide")

st.markdown(
    """
    ### ⚡ Derivatives — Rate of Change

    A **derivative** measures how fast a quantity changes.  
    It is the slope of the curve at any point.

    #### 🔍 Why Derivatives Matter in JEE
    - Used in optimization (maxima/minima).
    - Essential for motion problems (velocity, acceleration).
    - Required for curve sketching and tangent/normal questions.

    #### 🧠 Quick Example
    If f(x) = x², then f'(x) = 2x  
    This tells us how steep the curve is at any point.

    ---
    """
)

st.title("Derivatives")
run_derivatives()

# import streamlit as st
# from modules.differentiation.step_solver import derivative_steps

# st.title("Derivative Step Solver")

# expr_input = st.text_input("Enter a function of x", "sin(x)*x^2")

# if st.button("Solve"):
#     steps_text, steps_latex, final_answer = derivative_steps(expr_input)

#     st.subheader("Step-by-Step Solution")
#     st.text(steps_text)

#     st.subheader("LaTeX Steps")
#     st.markdown(steps_latex)

#     st.subheader("Final Answer")
#     st.latex(final_answer)

# # import streamlit as st
# # from modules.derivatives import run_derivatives

# # st.markdown(
# #     """
# #     ### ⚡ Derivatives — Rate of Change

# #     A **derivative** measures how fast a quantity changes.  
# #     It is the slope of the curve at any point.

# #     #### 🔍 Why Derivatives Matter in JEE
# #     - Used in optimization (maxima/minima).
# #     - Essential for motion problems (velocity, acceleration).
# #     - Required for curve sketching and tangent/normal questions.

# #     #### 🧠 Quick Example
# #     \nIf f(x) = x², then f'(x) = 2x  
# #     This tells us how steep the curve is at any point.

# #     ---
# #     """
# # )

# # st.set_page_config(page_title="Derivatives", layout="wide")
# # st.title("Derivatives")
# # run_derivatives()

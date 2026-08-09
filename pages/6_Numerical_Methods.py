import streamlit as st
from modules.numerical_methods import run_numerical

st.markdown(
    """
    ### 🔢 Numerical Methods

    Numerical methods approximate derivatives and integrals when exact solutions are hard.

    #### 🔍 Why Numerical Methods Matter
    - Helps understand how computers solve calculus.
    - Useful for engineering & data science.
    - Builds intuition for approximation techniques.

    #### 🧠 Quick Example
    \nTrapezoidal Rule approximates area by dividing the curve into trapezoids.

    ---
    """
)

st.set_page_config(page_title="Numerical Methods", layout="wide")
st.title("Numerical Methods")
run_numerical()

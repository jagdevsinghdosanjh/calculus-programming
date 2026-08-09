import streamlit as st
from modules.derivatives import run_derivatives

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
    \nIf f(x) = x², then f'(x) = 2x  
    This tells us how steep the curve is at any point.

    ---
    """
)

st.set_page_config(page_title="Derivatives", layout="wide")
st.title("Derivatives")
run_derivatives()

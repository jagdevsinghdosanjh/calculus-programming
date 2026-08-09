import streamlit as st
from modules.differential_eq import run_diff_eq

st.markdown(
    """
    ### 🔄 Differential Equations

    A **differential equation** relates a function with its derivatives.  
    They model real‑world phenomena like growth, decay, motion, and heat flow.

    #### 🔍 Why DEs Matter in JEE
    - First‑order linear DEs.
    - Variable separable DEs.
    - Growth/decay models.
    - Simple physics applications.

    #### 🧠 Quick Example
    \ndy/dx = ky → y = Ce^{kx}  
    This models exponential growth/decay.

    ---
    """
)


st.set_page_config(page_title="Differential Equations", layout="wide")
st.title("Differential Equations")
run_diff_eq()

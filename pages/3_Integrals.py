import streamlit as st
from modules.integrals import run_integrals
st.markdown(
    """
    ### 📐 Integrals — Area & Accumulation

    An **integral** measures the total accumulation of a quantity.  
    It can represent area, distance, work done, or total change.

    #### 🔍 Why Integrals Matter in JEE
    - Area under curves.
    - Definite integrals with limits.
    - Substitution & integration by parts.
    - Applications in physics (work, energy).

    #### 🧠 Quick Example
    \n∫ x dx = x²/2 + C  
    This gives the family of antiderivatives.

    ---
    """
)

st.set_page_config(page_title="Integrals", layout="wide")
st.title("Integrals")
run_integrals()

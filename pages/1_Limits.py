import streamlit as st
from modules.limits import run_limits
st.markdown(
    """
    ### 📘 Understanding Limits

    A **limit** tells us what value a function approaches as the input gets close to a particular point.  
    Limits form the foundation of **continuity**, **derivatives**, and **integrals** — making them essential for JEE.

    #### 🔍 Why Limits Matter in JEE
    - They help determine whether a function is continuous.
    - They are used to define derivatives.
    - Many JEE problems involve tricky limit expressions.

    #### 🧠 Quick Example
    \nAs x → 0, sin(x)/x → 1  
    This is one of the most important standard limits.

    ---
    """
)

st.set_page_config(page_title="Limits", layout="wide")
st.title("Limits")
run_limits()

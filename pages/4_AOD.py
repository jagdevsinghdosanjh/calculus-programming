import streamlit as st
from modules.aod import run_aod

st.markdown(
    """
    ### 📊 Applications of Derivatives (AOD)

    AOD helps us understand how functions behave — where they rise, fall, peak, or flatten.

    #### 🔍 Why AOD Matters in JEE
    - Maxima & minima problems.
    - Increasing/decreasing intervals.
    - Points of inflection.
    - Optimization word problems.

    #### 🧠 Quick Example
    \nIf f'(x) = 0 and f''(x) > 0 → Local Minimum  
    If f'(x) = 0 and f''(x) < 0 → Local Maximum

    ---
    """
)

st.set_page_config(page_title="Applications of Derivatives", layout="wide")
st.title("Applications of Derivatives")
run_aod()

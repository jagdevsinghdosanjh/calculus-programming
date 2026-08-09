import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import sympy as sp

from modules.aod import run_aod
from modules.derivatives import run_derivatives
from modules.differential_eq import run_diff_eq
from modules.integrals import run_integrals
from modules.limits import run_limits
from modules.numerical_methods import run_numerical


st.set_page_config(page_title="JEE Calculus Engine", layout="wide")

st.title("📘 JEE Calculus Programming Suite")
st.write("Run Class 11–12 calculus programs interactively.")

menu = st.sidebar.selectbox(
    "Select Topic",
    [
        "Limits",
        "Derivatives",
        "Integrals",
        "Applications of Derivatives",
        "Differential Equations",
        "Numerical Methods"
    ]
)

if menu == "Limits":
    run_limits()

elif menu == "Derivatives":
    run_derivatives()

elif menu == "Integrals":
    run_integrals()

elif menu == "Applications of Derivatives":
    run_aod()

elif menu == "Differential Equations":
    run_diff_eq()

elif menu == "Numerical Methods":
    run_numerical()

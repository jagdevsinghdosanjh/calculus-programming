import streamlit as st
from modules.numerical_methods import run_numerical

st.set_page_config(page_title="Numerical Methods", layout="wide")
st.title("Numerical Methods")
run_numerical()

import streamlit as st
from modules.derivatives import run_derivatives

st.set_page_config(page_title="Derivatives", layout="wide")
st.title("Derivatives")
run_derivatives()

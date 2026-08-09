import streamlit as st
from modules.integrals import run_integrals

st.set_page_config(page_title="Integrals", layout="wide")
st.title("Integrals")
run_integrals()

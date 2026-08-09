import streamlit as st
from modules.differential_eq import run_diff_eq

st.set_page_config(page_title="Differential Equations", layout="wide")
st.title("Differential Equations")
run_diff_eq()

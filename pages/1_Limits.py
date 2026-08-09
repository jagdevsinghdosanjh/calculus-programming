import streamlit as st
from modules.limits import run_limits

st.set_page_config(page_title="Limits", layout="wide")
st.title("Limits")
run_limits()

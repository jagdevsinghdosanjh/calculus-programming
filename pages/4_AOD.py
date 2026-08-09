import streamlit as st
from modules.aod import run_aod

st.set_page_config(page_title="Applications of Derivatives", layout="wide")
st.title("Applications of Derivatives")
run_aod()

import streamlit as st

st.markdown(
    """
    <div style="background: linear-gradient(90deg, #0F2027, #203A43, #2C5364);
                padding: 30px 20px; border-radius: 10px; margin-bottom: 25px;">
        <h1 style="color: white; text-align: center; font-family: 'Montserrat', sans-serif;">
            JEE Calculus Programming Suite
        </h1>
        <p style="color: #D9EAF7; text-align: center; font-size: 18px;
                  font-family: 'Montserrat', sans-serif;">
            Interactive Calculus Engine for Class 11–12 & JEE Main/Advanced
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="JEE Calculus Suite", layout="wide")

st.title("📘 JEE Calculus Programming Suite")
st.write("Welcome! Use the left sidebar to navigate through calculus modules.")

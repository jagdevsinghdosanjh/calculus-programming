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
st.markdown(
    """
    # 📘 Welcome to the JEE Calculus Programming Suite

    This interactive tool helps students explore and understand key calculus concepts used in **Class 11–12 and JEE Main/Advanced**.  
    Each module in the sidebar focuses on a specific topic and lets you **experiment, visualize, and compute** mathematical expressions instantly.

    ---

    ### 🔍 What you can do inside this app

    **Limits**  
    Understand how functions behave near a point. Useful for continuity, differentiability, and foundational JEE problems.

    **Derivatives**  
    Compute slopes, rates of change, and instantaneous velocity. Essential for physics, optimization, and JEE problem‑solving.

    **Integrals**  
    Evaluate areas, accumulated quantities, and antiderivatives. Supports both **indefinite** and **definite** integrals.

    **Applications of Derivatives (AOD)**  
    Find maxima, minima, turning points, and inflection points. Critical for optimization problems in JEE.

    **Differential Equations**  
    Solve first‑order ODEs symbolically. Useful for growth/decay models, motion, and advanced calculus.

    **Numerical Methods**  
    Approximate derivatives and integrals when exact solutions are difficult. Helps students understand how computers solve calculus problems.

    ---
    """,
    unsafe_allow_html=True
)

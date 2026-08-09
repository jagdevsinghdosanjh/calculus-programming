import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import sympy as sp

st.set_page_config(page_title="Math Solver", layout="wide")

st.markdown(
    """
    ### 🤖 Universal Math Solver (Like <a href="https://math.he.net/">math.he.net</a>)

    Enter any mathematical expression — derivative, integral, limit, equation, or function —  
    and this solver will automatically detect the type and compute the result.

    ---
    """
)

x = sp.Symbol("x")
y = sp.Function("y")(x)

expr_input = st.text_input("Enter any math expression:", "integrate(x)")

def safe_plot(expr):
    """Safely plot a SymPy expression."""
    try:
        f = sp.lambdify(x, expr, "numpy")
        xs = np.linspace(-10, 10, 400)
        ys = f(xs)

        fig, ax = plt.subplots()
        ax.plot(xs, ys)
        ax.set_title("Function Plot")
        st.pyplot(fig)
    except Exception:
        st.info("Plot unavailable for this expression.")

if expr_input:
    try:
        expr = sp.sympify(expr_input)

        st.write("### 🔍 Detected Expression")
        st.latex(expr)

        # ---------------------------------------------------------
        # 1. Integral
        # ---------------------------------------------------------
        if isinstance(expr, sp.Integral):
            st.subheader("📐 Integral Detected")

            integrand = expr.function
            var = expr.variables[0]

            st.write("### Step-by-step Explanation")
            st.write("1. Identify the integrand:")
            st.latex(integrand)

            st.write("2. Apply integration rules:")

            result = sp.integrate(integrand, var)
            st.success(f"Result: {result}")

            safe_plot(integrand)

        # ---------------------------------------------------------
        # 2. Derivative
        # ---------------------------------------------------------
        elif isinstance(expr, sp.Derivative):
            st.subheader("⚡ Derivative Detected")

            func = expr.expr
            var = expr.variables[0]

            st.write("### Step-by-step Explanation")
            st.write("1. Identify the function:")
            st.latex(func)

            st.write("2. Apply differentiation rules:")

            result = sp.diff(func, var)
            st.success(f"Result: {result}")

            safe_plot(result)

        # ---------------------------------------------------------
        # 3. Limit
        # ---------------------------------------------------------
        elif isinstance(expr, sp.Limit):
            st.subheader("📉 Limit Detected")

            func = expr.args[0]
            var = expr.args[1]
            point = expr.args[2]

            st.write("### Step-by-step Explanation")
            st.write("1. Identify the function approaching a point:")
            st.latex(func)

            st.write("2. Evaluate the limit:")

            result = sp.limit(func, var, point)
            st.success(f"Result: {result}")

        # ---------------------------------------------------------
        # 4. Equation solving
        # ---------------------------------------------------------
        elif isinstance(expr, sp.Equality):
            st.subheader("🧮 Equation Detected")

            st.write("### Solving Equation")
            result = sp.solve(expr, x)
            st.success(f"Solutions: {result}")

        # ---------------------------------------------------------
        # 5. Differential Equation
        # ---------------------------------------------------------
        elif isinstance(expr, sp.Eq) and expr.has(sp.Derivative):
            st.subheader("🔄 Differential Equation Detected")

            st.write("### Solving Differential Equation")
            result = sp.dsolve(expr)
            st.success(f"Solution: {result}")

        # ---------------------------------------------------------
        # 6. General Expression
        # ---------------------------------------------------------
        else:
            st.subheader("🧠 General Expression")

            result = sp.simplify(expr)
            st.success(f"Simplified: {result}")

            safe_plot(expr)

        # ---------------------------------------------------------
        # Mathbot-style interpretation
        # ---------------------------------------------------------
        st.write("---")
        st.write("### 🤖 Mathbot Interpretation")

        try:
            if hasattr(expr, "is_polynomial") and expr.is_polynomial():
                st.info("This is a polynomial expression.")
            elif hasattr(expr, "is_constant") and expr.is_constant():
                st.info("This is a constant expression.")
            elif hasattr(expr, "is_real") and expr.is_real:
                st.info("This expression evaluates to a real number.")
            else:
                st.info("This is a symbolic mathematical expression.")
        except Exception:
            st.info("Interpretation unavailable for this expression.")

    except (sp.SympifyError, ValueError) as e:
        st.error(f"Invalid expression: {e}")

# import streamlit as st
# import sympy as sp
# import numpy as np
# import matplotlib.pyplot as plt

# st.set_page_config(page_title="Math Solver", layout="wide")

# st.markdown(
#     """
#     ### 🤖 Universal Math Solver (Like math.he.net)

#     Enter any mathematical expression — derivative, integral, limit, equation, or function —  
#     and this solver will automatically detect the type and compute the result.

#     ---
#     """
# )

# x = sp.Symbol("x")
# y = sp.Function("y")(x)

# expr_input = st.text_input("Enter any math expression:", "integrate(x)")

# if expr_input:
#     try:
#         expr = sp.sympify(expr_input)

#         st.write("### 🔍 Detected Expression")
#         st.latex(expr)

#         # ---------------------------------------------------------
#         # 1. Detect Integrals
#         # ---------------------------------------------------------
#         if isinstance(expr, sp.Integral):
#             st.subheader("📐 Integral Detected")
#             st.write("### Step-by-step Explanation")
#             st.write("1. Identify the integrand.")
#             st.latex(expr.function)
#             st.write("2. Apply integration rules.")

#             result = sp.integrate(expr.function, expr.variables[0])
#             st.success(f"Result: {result}")

#             # Plot integrand
#             try:
#                 f = sp.lambdify(x, expr.function, "numpy")
#                 xs = np.linspace(-10, 10, 400)
#                 plt.plot(xs, f(xs))
#                 plt.title("Integrand Plot")
#                 st.pyplot(plt)
#             except Exception:
#                 st.info("Plot unavailable for this expression.")

#         # ---------------------------------------------------------
#         # 2. Detect Derivatives
#         # ---------------------------------------------------------
#         elif isinstance(expr, sp.Derivative):
#             st.subheader("⚡ Derivative Detected")
#             st.write("### Step-by-step Explanation")
#             st.write("1. Identify the function.")
#             st.latex(expr.expr)
#             st.write("2. Apply differentiation rules.")

#             result = sp.diff(expr.expr, expr.variables[0])
#             st.success(f"Result: {result}")

#             # Plot derivative
#             try:
#                 f = sp.lambdify(x, result, "numpy")
#                 xs = np.linspace(-10, 10, 400)
#                 plt.plot(xs, f(xs))
#                 plt.title("Derivative Plot")
#                 st.pyplot(plt)
#             except Exception:
#                 st.info("Plot unavailable for this derivative.")

#         # ---------------------------------------------------------
#         # 3. Detect Limits
#         # ---------------------------------------------------------
#         elif isinstance(expr, sp.Limit):
#             st.subheader("📉 Limit Detected")
#             st.write("### Step-by-step Explanation")
#             st.write("1. Identify the function approaching a point.")
#             st.latex(expr.args[0])
#             st.write("2. Evaluate the limit.")

#             result = sp.limit(expr.args[0], expr.args[1], expr.args[2])
#             st.success(f"Result: {result}")

#         # ---------------------------------------------------------
#         # 4. Detect Equations
#         # ---------------------------------------------------------
#         elif isinstance(expr, sp.Equality):
#             st.subheader("🧮 Equation Detected")
#             st.write("### Solving Equation")

#             result = sp.solve(expr, x)
#             st.success(f"Solutions: {result}")

#         # ---------------------------------------------------------
#         # 5. Detect Differential Equations
#         # ---------------------------------------------------------
#         elif isinstance(expr, sp.Eq) and expr.has(sp.Derivative):
#             st.subheader("🔄 Differential Equation Detected")
#             st.write("### Solving Differential Equation")

#             result = sp.dsolve(expr)
#             st.success(f"Solution: {result}")

#         # ---------------------------------------------------------
#         # 6. General Expression (Simplification)
#         # ---------------------------------------------------------
#         else:
#             st.subheader("🧠 General Expression")
#             st.write("### Simplified Form")

#             result = sp.simplify(expr)
#             st.success(f"Simplified: {result}")

#             # Plot if possible
#             try:
#                 f = sp.lambdify(x, expr, "numpy")
#                 xs = np.linspace(-10, 10, 400)
#                 plt.plot(xs, f(xs))
#                 plt.title("Function Plot")
#                 st.pyplot(plt)
#             except Exception:
#                 st.info("Plot unavailable for this expression.")

#         # ---------------------------------------------------------
#         # Mathbot-style interpretation
#         # ---------------------------------------------------------
#         st.write("---")
#         st.write("### 🤖 Mathbot Interpretation")

#         if expr.is_polynomial():
#             st.info("This is a polynomial expression.")
#         elif expr.is_constant():
#             st.info("This is a constant expression.")
#         elif expr.is_real:
#             st.info("This expression evaluates to a real number.")
#         else:
#             st.info("This is a symbolic mathematical expression.")

#     except Exception as e:
#         st.error(f"Error: {e}")

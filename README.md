<p align="center">
  <img src="banner.png" alt="JEE Calculus Suite Banner" width="100%">
</p>

<h1 align="center">📘 JEE Calculus Programming Suite</h1>
<p align="center">
Interactive Calculus Engine for Class 11–12 & JEE Main/Advanced<br>
Built with Streamlit • SymPy • NumPy • Matplotlib
</p>

📘 JEE Calculus Programming Suite
Interactive Calculus Engine built with Streamlit, SymPy, NumPy & Matplotlib
This project provides a modular, interactive calculus toolkit designed for Class 11–12 + JEE Main/Advanced students.
It runs entirely on Streamlit Cloud, allowing users to explore calculus concepts visually and interactively.

🚀 Live Demo (Streamlit Cloud)
Deploy your app instantly on Streamlit Cloud:

Code
https://share.streamlit.io/<your-username>/calculus-programming
(Replace <your-username> with your GitHub username once deployed.)

📂 Project Structure
Code
calculus-programming/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore venv, cache, build artifacts
│
└── modules/
    ├── limits.py              # Limits calculator
    ├── derivatives.py         # Derivatives engine
    ├── integrals.py           # Indefinite & definite integrals
    ├── aod.py                 # Applications of derivatives
    ├── differential_eq.py     # Differential equation solver
    └── numerical_methods.py   # Numerical calculus (derivative + integration)
Each module is fully isolated, lint‑clean (Ruff + Pylance), and production‑ready.

✨ Features
✔ Limits Calculator
Evaluate symbolic limits using SymPy.

✔ Derivatives Engine
Compute derivatives of algebraic, trigonometric, exponential, and composite functions.

✔ Integration Engine
Supports both indefinite and definite integrals.

✔ Applications of Derivatives (AOD)
Critical points

Maxima / Minima

Inflection points

✔ Differential Equation Solver
Solve first‑order ODEs using SymPy’s dsolve.

✔ Numerical Methods
Numerical derivative (finite difference)

Numerical integration (trapezoidal rule)

✔ Streamlit UI
Clean sidebar navigation with modular execution.

🛠 Installation (Local Development)
Clone the repository:

bash
git clone https://github.com/jagdevsinghdosanjh/calculus-programming
cd calculus-programming
Create a virtual environment:

bash
python -m venv .calculus-venv
Activate it:

bash
# Windows
.\.calculus-venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
☁️ Deploying to Streamlit Cloud
Push your project to GitHub

Visit: https://share.streamlit.io

Select your repository

Choose app.py as the entry point

Streamlit Cloud will auto‑install dependencies from requirements.txt

Your app will be live in seconds.

📦 requirements.txt
Code
streamlit
sympy
numpy
matplotlib
These packages are fully compatible with Streamlit Cloud.

🧹 .gitignore
Code
# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
.calculus-venv/
venv/
env/

# Streamlit
.streamlit/

# IDE settings
.vscode/
.idea/

# Jupyter
.ipynb_checkpoints/

# Build artifacts
build/
dist/
*.egg-info/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
📜 License
This project is open‑source and available under the MIT License.

👨‍💻 Author
Jagdev Singh Dosanjh  
Ed‑Tech Founder • Architect of Modular PCM Portal
Amritsar, Punjab, India

⭐ Contribute
Pull requests are welcome!
If you want additional modules (Vector Calculus, Laplace Transform, Fourier Series), feel free to open an issue.
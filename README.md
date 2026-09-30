# Data Science Practice Lab (3rd Semester)

Welcome to your Python Data Science practice workspace for **NumPy**, **Pandas**, and **Matplotlib**!

---

## 🚀 Getting Started

A dedicated virtual environment (`.venv`) has been created for you with all required packages installed.

### 1. Activating the Virtual Environment

In your terminal (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
*(If PowerShell shows an execution policy restriction, you can enable it for the current session with: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

Or run directly without activating:
```powershell
.\.venv\Scripts\python.exe <script_name>.py
```

### 2. Selecting Python in VS Code / Your IDE
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P`).
2. Type **Python: Select Interpreter**.
3. Choose the one pointing to:
   `e:\DATA SCIENCE\3RD SEM\.venv\Scripts\python.exe`
4. If you open or create Jupyter Notebooks (`.ipynb`), select the `.venv` kernel in the top-right corner.

---

## 📁 Practice Modules in This Folder

| File | Topic | What You Will Learn |
| :--- | :--- | :--- |
| [`verify_setup.py`](file:///e:/DATA%20SCIENCE/3RD%20SEM/verify_setup.py) | **Environment Verification** | Tests imports, displays library versions, and generates a sanity check plot. |
| [`01_numpy_practice.py`](file:///e:/DATA%20SCIENCE/3RD%20SEM/01_numpy_practice.py) | **NumPy Foundations** | Arrays, shapes, ndim, slicing, broadcasting, linear algebra, stats, reshaping. |
| [`02_pandas_practice.py`](file:///e:/DATA%20SCIENCE/3RD%20SEM/02_pandas_practice.py) | **Pandas Data Wrangling** | Series, DataFrames, `.loc`/`.iloc`, filtering, handling `NaN`s, `groupby`, CSV I/O. |
| [`03_matplotlib_practice.py`](file:///e:/DATA%20SCIENCE/3RD%20SEM/03_matplotlib_practice.py) | **Data Visualization** | Line plots, bar charts, histograms, scatter plots, 2x2 multi-panel subplots. |
| [`04_data_analysis_workflow.py`](file:///e:/DATA%20SCIENCE/3RD%20SEM/04_data_analysis_workflow.py) | **Integrated Mini-Project** | End-to-end sales analytics pipeline combining NumPy + Pandas + Matplotlib. |

---

## 🏃 Running the Scripts

Run any script from the terminal:
```powershell
# Verify installation
.\.venv\Scripts\python.exe verify_setup.py

# Run NumPy practice
.\.venv\Scripts\python.exe 01_numpy_practice.py

# Run Pandas practice
.\.venv\Scripts\python.exe 02_pandas_practice.py

# Run Matplotlib practice (generates PNG image files)
.\.venv\Scripts\python.exe 03_matplotlib_practice.py

# Run Full Integrated Project
.\.venv\Scripts\python.exe 04_data_analysis_workflow.py
```

---

## 🧠 Quick Cheat Sheet

### NumPy
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mat = np.zeros((3, 3))             # 3x3 zeros
r = np.arange(0, 10, 2)            # [0, 2, 4, 6, 8]
filt = arr[arr > 2]                # Boolean masking
mean_val = arr.mean()              # Mean
dot_prod = A @ B                   # Matrix multiplication
```

### Pandas
```python
import pandas as pd

df = pd.read_csv("data.csv")       # Load CSV
df.head(5)                         # First 5 rows
df.describe()                      # Statistical summary
filtered = df[df["GPA"] > 3.5]     # Condition filtering
grouped = df.groupby("Dept").mean()# Groupby aggregation
df.fillna(df.median(), inplace=True)# Impute missing values
```

### Matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color="blue", marker="o", label="Trend")
ax.set_title("My Chart Title")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()
ax.grid(True)
plt.savefig("chart.png", dpi=150)
plt.show()
```

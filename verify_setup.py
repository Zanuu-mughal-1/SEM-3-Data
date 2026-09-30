"""
Verification Script for Data Science Practice Environment
Tests imports of NumPy, Pandas, Matplotlib, and Seaborn.
"""
import sys

def verify_environment():
    print("=" * 60)
    print(" DATA SCIENCE ENVIRONMENT VERIFICATION ")
    print("=" * 60)
    print(f"Python Executable: {sys.executable}")
    print(f"Python Version   : {sys.version.split()[0]}")
    print("-" * 60)

    modules = ["numpy", "pandas", "matplotlib", "seaborn", "ipykernel", "openpyxl"]
    success = True

    for mod in modules:
        try:
            m = __import__(mod)
            version = getattr(m, "__version__", "unknown")
            print(f"  [OK] {mod:<12} (version: {version})")
        except ImportError as e:
            print(f"  [FAILED] {mod:<12} - Error: {e}")
            success = False

    print("-" * 60)
    if success:
        # Quick sanity check: generate a test plot and sample dataframe
        import numpy as np
        import pandas as pd
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive backend for headless execution
        import matplotlib.pyplot as plt

        print("\nRunning quick functionality check...")
        # 1. NumPy sanity test
        arr = np.array([1, 2, 3, 4, 5])
        print(f" - NumPy array mean: {arr.mean()} (Expected: 3.0)")

        # 2. Pandas sanity test
        df = pd.DataFrame({
            "Topic": ["NumPy", "Pandas", "Matplotlib"],
            "Status": ["Ready", "Ready", "Ready"]
        })
        print(" - Pandas DataFrame preview:")
        print(df.to_string(index=False))

        # 3. Matplotlib sanity test
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(["Day 1", "Day 2", "Day 3", "Day 4"], [10, 25, 45, 80], marker='o', color='#2563eb', linewidth=2)
        ax.set_title("Data Science Learning Curve - Verification Plot", fontsize=12, fontweight='bold')
        ax.set_ylabel("Confidence (%)")
        ax.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plot_path = "verification_plot.png"
        plt.savefig(plot_path, dpi=120)
        plt.close(fig)
        print(f" - Matplotlib test plot saved to: {plot_path}")

        print("\nAll checks passed successfully! Your environment is ready for practice.")
    else:
        print("\nSome libraries are missing. Please run pip install -r requirements.txt")

    print("=" * 60)

if __name__ == "__main__":
    verify_environment()

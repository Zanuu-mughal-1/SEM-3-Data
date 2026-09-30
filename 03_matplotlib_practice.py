"""
================================================================================
MATPLOTLIB PRACTICE LAB - DATA SCIENCE 3RD SEMESTER
================================================================================
Matplotlib is the core plotting library in Python. It provides fine-grained
control over charts, axes, colors, and publication-quality figures.

Run this script in terminal:
    python 03_matplotlib_practice.py
================================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

def section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def part_1_line_plot():
    section("1. LINE PLOT: CUSTOM STYLING & LABELS")

    # Generate synthetic study time vs exam score data
    hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    student_scores = np.array([52, 58, 64, 69, 75, 80, 86, 91, 95, 98])
    peer_avg_scores = np.array([50, 55, 60, 65, 70, 75, 78, 82, 85, 88])

    fig, ax = plt.subplots(figsize=(8, 4.5))

    ax.plot(hours_studied, student_scores, color="#2563eb", marker="o", linewidth=2.5, label="Student Score")
    ax.plot(hours_studied, peer_avg_scores, color="#dc2626", linestyle="--", linewidth=2, label="Peer Average")

    ax.set_title("Study Hours vs Exam Score", fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Hours Studied per Week", fontsize=11)
    ax.set_ylabel("Exam Score (Out of 100)", fontsize=11)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(frameon=True, loc="lower right")

    plt.tight_layout()
    output_path = "01_line_plot.png"
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f" Saved Line Plot to: {output_path}")


def part_2_bar_chart():
    section("2. BAR CHARTS: CATEGORICAL DATA")

    departments = ["Data Science", "Computer Sci", "AI & Robotics", "Software Eng", "Cyber Security"]
    student_counts = [120, 185, 95, 140, 80]
    colors = ["#3b82f6", "#10b981", "#8b5cf6", "#f59e0b", "#ef4444"]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.bar(departments, student_counts, color=colors, edgecolor="black", linewidth=0.8, width=0.6)

    # Add data value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f"{height}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha="center", va="bottom", fontweight="bold")

    ax.set_title("3rd Semester Enrollment by Department", fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Department", fontsize=11)
    ax.set_ylabel("Number of Students", fontsize=11)
    ax.set_ylim(0, 220)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    output_path = "02_bar_chart.png"
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f" Saved Bar Chart to: {output_path}")


def part_3_scatter_and_histogram():
    section("3. SCATTER PLOTS & HISTOGRAMS")

    np.random.seed(42)
    # Generate 150 student records
    gpa = np.random.normal(3.2, 0.4, 150).clip(2.0, 4.0)
    study_hours = gpa * 7.5 + np.random.normal(0, 3, 150)
    study_hours = study_hours.clip(5, 40)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Scatter Plot
    scatter = ax1.scatter(study_hours, gpa, c=gpa, cmap="viridis", alpha=0.8, edgecolors="none", s=50)
    ax1.set_title("Study Hours vs GPA (Scatter)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Weekly Study Hours")
    ax1.set_ylabel("GPA")
    ax1.grid(True, linestyle=":", alpha=0.5)
    fig.colorbar(scatter, ax=ax1, label="GPA Scale")

    # 2. Histogram
    ax2.hist(gpa, bins=15, color="#14b8a6", edgecolor="white", alpha=0.85)
    ax2.axvline(gpa.mean(), color="#b91c1c", linestyle="--", linewidth=2, label=f"Mean: {gpa.mean():.2f}")
    ax2.set_title("GPA Distribution (Histogram)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("GPA")
    ax2.set_ylabel("Frequency")
    ax2.legend()
    ax2.grid(axis="y", linestyle=":", alpha=0.5)

    plt.tight_layout()
    output_path = "03_scatter_histogram.png"
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f" Saved Scatter & Histogram Subplots to: {output_path}")


def part_4_multi_panel_dashboard():
    section("4. 2x2 MULTI-PANEL SUBPLOT DASHBOARD")

    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_exp = np.exp(x / 3)
    categories = ["Quiz 1", "Quiz 2", "Midterm", "Final"]
    box_data = [
        np.random.normal(70, 10, 50),
        np.random.normal(75, 8, 50),
        np.random.normal(68, 12, 50),
        np.random.normal(82, 9, 50)
    ]

    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    # Panel (0, 0): Trigonometric Curves
    axes[0, 0].plot(x, y_sin, label="sin(x)", color="navy")
    axes[0, 0].plot(x, y_cos, label="cos(x)", color="darkorange", linestyle="--")
    axes[0, 0].set_title("Sine & Cosine Waves")
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Panel (0, 1): Exponential Curve
    axes[0, 1].plot(x, y_exp, color="darkgreen", linewidth=2)
    axes[0, 1].set_title("Exponential Growth")
    axes[0, 1].grid(True, alpha=0.3)

    # Panel (1, 0): Boxplot of Exam Scores
    axes[1, 0].boxplot(box_data, tick_labels=categories, patch_artist=True,
                       boxprops=dict(facecolor="#c7d2fe", color="#3730a3"),
                       medianprops=dict(color="#1e1b4b", linewidth=2))
    axes[1, 0].set_title("Score Distributions (Box Plot)")
    axes[1, 0].set_ylabel("Marks")
    axes[1, 0].grid(axis="y", alpha=0.3)

    # Panel (1, 1): Pie Chart of Grade Breakdown
    grade_labels = ["A Grade", "B Grade", "C Grade", "Below C"]
    grade_sizes = [30, 45, 18, 7]
    grade_colors = ["#22c55e", "#3b82f6", "#f59e0b", "#ef4444"]
    axes[1, 1].pie(grade_sizes, labels=grade_labels, autopct="%1.1f%%", colors=grade_colors,
                   startangle=140, explode=(0.08, 0, 0, 0))
    axes[1, 1].set_title("Overall Grade Distribution (Pie Chart)")

    fig.suptitle("Data Science Visualization Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout()
    output_path = "04_visualization_dashboard.png"
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f" Saved Multi-Panel Dashboard to: {output_path}")


def hands_on_exercises():
    section("5. HANDS-ON PRACTICE EXERCISES")
    print("""
Try creating your own charts:

Exercise 1: Create a line plot displaying monthly temperature variation for a year.
            Add labels, custom line color, and marker.

Exercise 2: Create a horizontal bar chart comparing 5 programming languages
            by popularity.
            Hint: ax.barh(languages, popularity)

Exercise 3: Create a 1x2 subplot figure comparing raw data histogram on the left
            and log-transformed data histogram on the right.
    """)


if __name__ == "__main__":
    part_1_line_plot()
    part_2_bar_chart()
    part_3_scatter_and_histogram()
    part_4_multi_panel_dashboard()
    hands_on_exercises()

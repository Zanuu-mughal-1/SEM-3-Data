"""
================================================================================
MINI PROJECT: INTEGRATED DATA SCIENCE WORKFLOW (NumPy + Pandas + Matplotlib)
================================================================================
This script demonstrates how NumPy, Pandas, and Matplotlib collaborate in
a real-world Data Science workflow:
  1. NumPy      -> Data generation, array transformations & simulation
  2. Pandas     -> Cleaning, reshaping, aggregating, and statistical grouping
  3. Matplotlib -> Visual communication and multi-chart reporting

Run this script in terminal:
    python 04_data_analysis_workflow.py
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_pipeline():
    print("=" * 65)
    print(" STEP 1: NUMPY SIMULATION OF E-COMMERCE STORE SALES DATA ")
    print("=" * 65)

    np.random.seed(42)
    n_records = 300

    # Generate dates across 30 days
    date_offsets = np.random.randint(0, 30, size=n_records)
    base_date = pd.Timestamp("2026-09-01")
    order_dates = [base_date + pd.Timedelta(days=int(d)) for d in date_offsets]

    # Categories and base prices
    categories = np.random.choice(["Electronics", "Books", "Fashion", "Home & Kitchen"], size=n_records, p=[0.25, 0.20, 0.35, 0.20])
    quantities = np.random.randint(1, 5, size=n_records)

    # Unit price based on category
    category_prices = {
        "Electronics": (80, 500),
        "Books": (10, 50),
        "Fashion": (20, 150),
        "Home & Kitchen": (30, 200)
    }

    unit_prices = np.array([
        np.round(np.random.uniform(*category_prices[cat]), 2)
        for cat in categories
    ])

    # Customer ratings between 1.0 and 5.0
    ratings = np.round(np.random.normal(loc=4.1, scale=0.8, size=n_records).clip(1.0, 5.0), 1)

    # Insert some missing ratings to practice cleaning
    missing_indices = np.random.choice(n_records, size=15, replace=False)
    ratings[missing_indices] = np.nan

    print(f"Generated {n_records} simulated sales transactions using NumPy.")

    print("\n" + "=" * 65)
    print(" STEP 2: PANDAS WRANGLING & AGGREGATIONS ")
    print("=" * 65)

    df = pd.DataFrame({
        "OrderDate": order_dates,
        "Category": categories,
        "Quantity": quantities,
        "UnitPrice": unit_prices,
        "Rating": ratings
    })

    # Computed column: Total Sales
    df["TotalRevenue"] = df["Quantity"] * df["UnitPrice"]

    print("Sample Transactions:")
    print(df.head(5))

    # Missing value handling
    missing_count = df["Rating"].isna().sum()
    print(f"\nMissing Ratings Count: {missing_count}")
    df["Rating"] = df["Rating"].fillna(df["Rating"].median())
    print("Imputed missing ratings with median value.")

    # Grouped metrics by Category
    category_summary = df.groupby("Category").agg(
        Total_Orders=("Quantity", "count"),
        Total_Items_Sold=("Quantity", "sum"),
        Total_Revenue=("TotalRevenue", "sum"),
        Average_Order_Value=("TotalRevenue", "mean"),
        Average_Rating=("Rating", "mean")
    ).reset_index()

    print("\nCategory Summary Statistics:")
    print(category_summary.to_string(index=False))

    # Daily trend
    daily_sales = df.groupby("OrderDate")["TotalRevenue"].sum().sort_index()

    print("\n" + "=" * 65)
    print(" STEP 3: MATPLOTLIB VISUAL DASHBOARD CREATION ")
    print("=" * 65)

    fig = plt.figure(figsize=(14, 8))
    fig.patch.set_facecolor("#f8fafc")

    # Layout: 2 rows, 2 columns
    # Panel 1: Daily Revenue Trend (Line Plot)
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(daily_sales.index.strftime('%b %d'), daily_sales.values, color="#2563eb", marker="o", markersize=4, linewidth=2)
    ax1.set_title("Daily Sales Trend (September 2026)", fontsize=11, fontweight="bold")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Revenue ($)")
    ax1.tick_params(axis="x", rotation=45)
    ax1.grid(True, linestyle=":", alpha=0.5)

    # Panel 2: Total Revenue by Category (Bar Chart)
    ax2 = plt.subplot(2, 2, 2)
    palette = ["#3b82f6", "#10b981", "#8b5cf6", "#f59e0b"]
    bars = ax2.bar(category_summary["Category"], category_summary["Total_Revenue"], color=palette, edgecolor="black", alpha=0.9)
    for bar in bars:
        height = bar.get_height()
        ax2.annotate(f"${height:,.0f}",
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax2.set_title("Total Revenue by Product Category", fontsize=11, fontweight="bold")
    ax2.set_ylabel("Revenue ($)")
    ax2.grid(axis="y", linestyle=":", alpha=0.5)

    # Panel 3: Customer Satisfaction Ratings (Histogram)
    ax3 = plt.subplot(2, 2, 3)
    ax3.hist(df["Rating"], bins=10, color="#ec4899", edgecolor="white", alpha=0.85)
    ax3.axvline(df["Rating"].mean(), color="#4b5563", linestyle="--", linewidth=2, label=f"Mean: {df['Rating'].mean():.2f}")
    ax3.set_title("Customer Rating Distribution", fontsize=11, fontweight="bold")
    ax3.set_xlabel("Rating (1-5 Stars)")
    ax3.set_ylabel("Frequency")
    ax3.legend()
    ax3.grid(axis="y", linestyle=":", alpha=0.5)

    # Panel 4: Unit Price vs Quantity Sold (Scatter Plot)
    ax4 = plt.subplot(2, 2, 4)
    scatter = ax4.scatter(df["UnitPrice"], df["Quantity"], c=df["TotalRevenue"], cmap="plasma", alpha=0.7, edgecolors="none")
    ax4.set_title("Unit Price vs Quantity (Colored by Total Revenue)", fontsize=11, fontweight="bold")
    ax4.set_xlabel("Unit Price ($)")
    ax4.set_ylabel("Quantity Purchased")
    ax4.set_yticks([1, 2, 3, 4])
    fig.colorbar(scatter, ax=ax4, label="Total Revenue ($)")
    ax4.grid(True, linestyle=":", alpha=0.5)

    fig.suptitle("E-Commerce Store Analytics: Integrated NumPy, Pandas & Matplotlib Report", fontsize=14, fontweight="bold", y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    output_filename = "04_ecommerce_analytics_report.png"
    plt.savefig(output_filename, dpi=150)
    plt.close(fig)

    print(f"Report generated successfully: {output_filename}")
    print("=" * 65)

if __name__ == "__main__":
    run_pipeline()

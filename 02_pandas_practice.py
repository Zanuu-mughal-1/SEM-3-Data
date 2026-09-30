"""
================================================================================
PANDAS PRACTICE LAB - DATA SCIENCE 3RD SEMESTER
================================================================================
Pandas is the premier data manipulation and analysis library for Python.
It introduces two essential data structures: Series (1D) and DataFrame (2D).

Run this script in terminal:
    python 02_pandas_practice.py
================================================================================
"""

import pandas as pd
import numpy as np

def section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def part_1_series_and_dataframes():
    section("1. SERIES & DATAFRAMES CREATION")

    # Pandas Series (1D labeled array)
    ages = pd.Series([21, 22, 20, 23], index=["Alice", "Bob", "Charlie", "David"], name="Age")
    print("Pandas Series:\n", ages)
    print(f"Alice's Age: {ages['Alice']}")

    # Pandas DataFrame (2D tabular structure)
    data = {
        "StudentID": [101, 102, 103, 104, 105, 106],
        "Name": ["Zain", "Sarah", "Ali", "Fatima", "Bilal", "Ayesha"],
        "Department": ["Computer Science", "Data Science", "Data Science", "Computer Science", "AI", "AI"],
        "Semester": [3, 3, 3, 3, 3, 3],
        "GPA": [3.65, 3.88, 3.40, 3.92, 3.10, 3.75],
        "Absences": [2, 0, 4, 1, 6, 0]
    }
    df = pd.DataFrame(data)
    print("\nStudent DataFrame:\n", df)

    # DataFrame inspection tools
    print("\nShape (rows, cols):", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nSummary Statistics (df.describe()):\n", df.describe())
    return df


def part_2_selection_and_filtering(df):
    section("2. SELECTION (loc, iloc) & FILTERING")

    # Column selection
    print("Single Column (df['GPA']):\n", df["GPA"].head(3))
    print("\nMultiple Columns:\n", df[["Name", "Department", "GPA"]].head(3))

    # Integer-based indexing: .iloc[row_idx, col_idx]
    print("\nFirst row using .iloc[0]:\n", df.iloc[0])
    print("\nRows 0 to 2, Columns 1 to 3:\n", df.iloc[0:3, 1:4])

    # Label-based indexing: .loc[row_label, col_label]
    print("\nUsing .loc with condition (GPA > 3.70):\n", df.loc[df["GPA"] > 3.70, ["Name", "Department", "GPA"]])

    # Multiple conditions using & (AND), | (OR)
    ds_high_gpa = df[(df["Department"] == "Data Science") & (df["GPA"] >= 3.50)]
    print("\nData Science students with GPA >= 3.50:\n", ds_high_gpa[["Name", "GPA"]])


def part_3_transformations_and_cleaning(df):
    section("3. DATA MANIPULATION & HANDLING MISSING VALUES")

    # Adding new computed columns
    df_copy = df.copy()
    df_copy["Attendance_Score"] = 100 - (df_copy["Absences"] * 10)
    df_copy["Passed_Dean_List"] = df_copy["GPA"] >= 3.70
    print("DataFrame with new columns:\n", df_copy[["Name", "Attendance_Score", "Passed_Dean_List"]])

    # Missing Data Handling Demonstration
    dirty_data = pd.DataFrame({
        "A": [1, 2, np.nan, 4, 5],
        "B": [10.5, np.nan, np.nan, 40.2, 50.1],
        "C": ["cat", "dog", "cat", None, "dog"]
    })
    print("\nDirty DataFrame with Missing Values (NaN):\n", dirty_data)

    print("\nChecking null counts (df.isna().sum()):\n", dirty_data.isna().sum())

    # Fill missing values
    cleaned_df = dirty_data.copy()
    cleaned_df["A"] = cleaned_df["A"].fillna(cleaned_df["A"].median())
    cleaned_df["B"] = cleaned_df["B"].fillna(cleaned_df["B"].mean())
    cleaned_df["C"] = cleaned_df["C"].fillna("Unknown")
    print("\nCleaned DataFrame after imputing (fillna):\n", cleaned_df)


def part_4_groupby_and_aggregation(df):
    section("4. GROUPBY & AGGREGATIONS")

    # Average GPA and Total Absences per Department
    dept_summary = df.groupby("Department").agg(
        Student_Count=("StudentID", "count"),
        Average_GPA=("GPA", "mean"),
        Max_GPA=("GPA", "max"),
        Total_Absences=("Absences", "sum")
    ).reset_index()

    print("Department-level GroupBy Summary:\n", dept_summary)


def part_5_file_io(df):
    section("5. READING & WRITING CSV FILES")

    csv_file = "students_practice_data.csv"
    df.to_csv(csv_file, index=False)
    print(f"Saved DataFrame to CSV: {csv_file}")

    # Read back from CSV
    loaded_df = pd.read_csv(csv_file)
    print(f"Successfully reloaded {len(loaded_df)} rows from CSV.")


def hands_on_exercises():
    section("6. HANDS-ON PRACTICE EXERCISES")
    print("""
Try these exercises to test your Pandas skills:

Exercise 1: Create a DataFrame representing 5 products with columns:
            'Product', 'Category', 'Price', 'Stock'
            Filter out products where 'Stock' is less than 10.

Exercise 2: Sort the student DataFrame by 'GPA' in descending order.
            Hint: df.sort_values(by='GPA', ascending=False)

Exercise 3: Group the products by 'Category' and calculate the total stock value:
            (Price * Stock) per category.
    """)

    # Demonstration of Exercise 2:
    demo_df = pd.DataFrame({
        "Name": ["Zain", "Sarah", "Ali", "Fatima"],
        "GPA": [3.65, 3.88, 3.40, 3.92]
    })
    sorted_df = demo_df.sort_values(by="GPA", ascending=False)
    print("--- Exercise 2 Demo Output (Sorted by GPA desc) ---")
    print(sorted_df.to_string(index=False))


if __name__ == "__main__":
    df = part_1_series_and_dataframes()
    part_2_selection_and_filtering(df)
    part_3_transformations_and_cleaning(df)
    part_4_groupby_and_aggregation(df)
    part_5_file_io(df)
    hands_on_exercises()

"""
================================================================================
NUMPY PRACTICE LAB - DATA SCIENCE 3RD SEMESTER
================================================================================
NumPy (Numerical Python) is the foundational library for scientific computing
in Python. It provides high-performance multidimensional arrays and tools.

Run this script in terminal:
    python 01_numpy_practice.py
================================================================================
"""

import numpy as np

def section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def part_1_array_creation():
    section("1. ARRAY CREATION & ATTRIBUTES")

    # Creating arrays from Python lists
    arr_1d = np.array([10, 20, 30, 40, 50])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("1D Array:", arr_1d)
    print("2D Array:\n", arr_2d)

    # Key attributes
    print(f"\n2D Array Shape   : {arr_2d.shape}  (rows, columns)")
    print(f"Dimensions (ndim): {arr_2d.ndim}")
    print(f"Data type (dtype): {arr_2d.dtype}")
    print(f"Total elements   : {arr_2d.size}")

    # Built-in creation functions
    zeros = np.zeros((2, 4))               # 2x4 matrix of zeros
    ones = np.ones((3, 3))                 # 3x3 matrix of ones
    range_arr = np.arange(0, 20, 2)        # start, stop (exclusive), step
    linear_space = np.linspace(0, 1, 5)    # 5 evenly spaced values between 0 and 1
    identity = np.eye(3)                   # 3x3 Identity matrix

    print("\nnp.zeros((2, 4)):\n", zeros)
    print("np.arange(0, 20, 2):", range_arr)
    print("np.linspace(0, 1, 5):", linear_space)
    print("np.eye(3):\n", identity)

    # Random generation
    np.random.seed(42)  # For reproducibility
    rand_uniform = np.random.rand(2, 3)          # Uniform [0, 1)
    rand_normal = np.random.randn(2, 3)          # Standard normal distribution (mean 0, std 1)
    rand_ints = np.random.randint(1, 100, size=(3, 3))  # Integers in [1, 100)

    print("\nnp.random.randint(1, 100, (3,3)):\n", rand_ints)


def part_2_indexing_and_slicing():
    section("2. INDEXING, SLICING & BOOLEAN MASKING")

    matrix = np.array([
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120]
    ])
    print("Original Matrix (3x4):\n", matrix)

    # Specific element: matrix[row, col]
    print("\nElement at row 1, col 2:", matrix[1, 2])  # 70

    # Row and column slicing
    print("First row (matrix[0, :])     :", matrix[0, :])
    print("Third column (matrix[:, 2])  :", matrix[:, 2])
    print("Sub-matrix (first 2 rows, cols 1-2):\n", matrix[:2, 1:3])

    # Boolean Masking (Crucial for Data Science filtering)
    greater_than_50 = matrix > 50
    print("\nBoolean condition (matrix > 50):\n", greater_than_50)
    print("Filtered elements (matrix[matrix > 50]):\n", matrix[greater_than_50])


def part_3_operations_and_broadcasting():
    section("3. VECTORIZED OPERATIONS & BROADCASTING")

    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    # Element-wise operations (No for-loops required!)
    print("a + b :", a + b)
    print("a * b :", a * b)
    print("a ** 2:", a ** 2)

    # Broadcasting: arithmetic between different shaped arrays
    mat = np.ones((3, 3)) * 5
    row_vector = np.array([1, 2, 3])
    print("\nMatrix (3x3 with 5s):\n", mat)
    print("Broadcasting row_vector [1, 2, 3] across rows:\n", mat + row_vector)

    # Matrix multiplication: @ operator or np.dot()
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("\nMatrix Multiplication (A @ B):\n", A @ B)


def part_4_aggregations_and_statistics():
    section("4. AGGREGATION & STATISTICS")

    scores = np.array([
        [75, 82, 90],
        [60, 88, 79],
        [95, 91, 85],
        [50, 70, 65]
    ])
    print("Exam Scores (4 students, 3 subjects):\n", scores)

    print(f"\nOverall Mean Score : {scores.mean():.2f}")
    print(f"Overall Std Dev    : {scores.std():.2f}")
    print(f"Overall Max Score  : {scores.max()}")

    # Aggregation along axes:
    # axis=0 -> along columns (per subject)
    # axis=1 -> along rows (per student)
    print("\nSubject Averages (axis=0):", scores.mean(axis=0))
    print("Student Averages (axis=1):", scores.mean(axis=1))
    print("Index of top student for each subject (argmax, axis=0):", scores.argmax(axis=0))


def part_5_reshaping_and_manipulation():
    section("5. RESHAPING & STACKING")

    arr = np.arange(12)
    print("1D array (12 elements):", arr)

    reshaped = arr.reshape(3, 4)
    print("Reshaped to 3x4:\n", reshaped)

    flattened = reshaped.flatten()
    print("Flattened back to 1D:", flattened)

    transposed = reshaped.T
    print("Transposed (4x3):\n", transposed)

    # Stacking
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print("\nVertical Stack (vstack):\n", np.vstack([x, y]))
    print("Horizontal Stack (hstack):\n", np.hstack([x, y]))


def hands_on_exercises():
    section("6. HANDS-ON PRACTICE EXERCISES")
    print("""
Now try completing these exercises! You can write your solutions directly
in this file or create your own notebook:

Exercise 1: Create a 5x5 matrix with values from 1 to 25.
            Extract the 3x3 center core of this matrix.
            Hint: matrix[1:4, 1:4]

Exercise 2: Create a random 1D array of 20 integers between 1 and 100.
            Replace all values greater than 50 with -1.
            Hint: arr[arr > 50] = -1

Exercise 3: Normalize a 1D array (x - mean) / std.
            Verify that the resulting array has mean approx 0 and std approx 1.
    """)

    # Demonstration of Exercise 1 solution:
    print("--- Exercise 1 Demo Solution ---")
    full_mat = np.arange(1, 26).reshape(5, 5)
    print("Full 5x5 Matrix:\n", full_mat)
    center_core = full_mat[1:4, 1:4]
    print("3x3 Center Core:\n", center_core)


if __name__ == "__main__":
    part_1_array_creation()
    part_2_indexing_and_slicing()
    part_3_operations_and_broadcasting()
    part_4_aggregations_and_statistics()
    part_5_reshaping_and_manipulation()
    hands_on_exercises()

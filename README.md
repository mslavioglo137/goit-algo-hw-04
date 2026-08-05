# Homework 4

## Overview

This repository contains solutions for Homework 4 on recursion and sorting algorithms.

The project consists of three tasks:

- Recursive file sorting by extension.
- Drawing the Koch Snowflake using recursion.
- Comparing sorting algorithms using execution time measurements.

---

# Task 1. Recursive File Sorting

## Description

This program recursively scans the source directory, copies all files to the destination directory, and automatically sorts them into subdirectories based on file extensions.

### Features

- Recursive directory traversal
- Automatic creation of destination folders
- File grouping by extension
- Exception handling
- Default destination folder (`dist`)
- Interactive directory selection

---

# Task 2. Koch Snowflake

## Description

This program draws the Koch Snowflake using a recursive algorithm.

The user specifies:

- recursion level;
- snowflake size.

### Features

- Recursive implementation
- Input validation
- User-friendly interface
- Recommended snowflake size
- Centered drawing
- Turtle graphics visualization

---

# Task 3. Sorting Algorithms Comparison

## Description

Three sorting algorithms were compared:

- Insertion Sort
- Merge Sort
- Python built-in Timsort (`sorted()`)

The comparison was performed using the `timeit` module.

Three different datasets were generated:

- Random
- Nearly sorted
- Reverse sorted

Each algorithm was tested on arrays containing:

- 100 elements
- 1,000 elements
- 5,000 elements
- 10,000 elements

---

## Results

The benchmark demonstrates that:

- **Insertion Sort** performs well only on small datasets but becomes significantly slower as the dataset grows because of its quadratic time complexity.
- **Merge Sort** provides stable performance with approximately **O(n log n)** complexity and is much faster than Insertion Sort on large datasets.
- **Timsort**, which is used internally by Python, consistently showed the best performance. It is highly optimized and especially efficient for partially sorted data.

---

## Conclusion

The experimental results confirm the theoretical complexity of the algorithms.

Although implementing classic sorting algorithms is useful for understanding their principles, Python's built-in **Timsort** is the preferred choice for real-world applications because it combines the advantages of Merge Sort and Insertion Sort while being highly optimized.

---

## Technologies

- Python 3
- recursion
- turtle
- pathlib
- shutil
- argparse
- random
- timeit
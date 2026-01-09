"""
AI Assignment - Week 1
Python Fundamentals for AI / ML
Author: Dinisha Jain
Purpose: Internship Assignment Submission
"""

# =====================================================
# Task 1: Python Basics & Operators
# =====================================================

def basic_operations():
    """Perform arithmetic, comparison, and logical operations"""

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\n--- Arithmetic Operations ---")
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")

    if num2 != 0:
        print(f"Division: {num1 / num2}")
        print(f"Modulus: {num1 % num2}")
    else:
        print("Division and Modulus not possible (division by zero).")

    print(f"Power: {num1 ** num2}")

    print("\n--- Comparison Operators ---")
    print(f"{num1} > {num2}: {num1 > num2}")
    print(f"{num1} < {num2}: {num1 < num2}")
    print(f"{num1} == {num2}: {num1 == num2}")
    print(f"{num1} != {num2}: {num1 != num2}")

    print("\n--- Logical Operators ---")
    print(f"Both positive: {num1 > 0 and num2 > 0}")
    print(f"At least one positive: {num1 > 0 or num2 > 0}")
    print(f"Not positive (num1): {not (num1 > 0)}")


# =====================================================
# Task 2: Lists and NumPy Arrays
# =====================================================

import random
import numpy as np

def list_and_array_operations():
    """Perform list and NumPy array operations"""

    numbers = [random.randint(1, 100) for _ in range(10)]
    print("\nOriginal List:", numbers)

    numbers.append(50)
    numbers.pop(0)

    print("Modified List:", numbers)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

    numbers.sort()
    print("Sorted List:", numbers)

    array = np.array(numbers)

    print("\n--- NumPy Statistics ---")
    print("Mean:", np.mean(array))
    print("Median:", np.median(array))
    print("Standard Deviation:", np.std(array))


# =====================================================
# Task 3: Dictionaries and Sets
# =====================================================

def dictionary_and_sets():
    """Work with dictionary and set data structures"""

    student = {
        "name": "Dinisha Jain",
        "course": "BSc Computer Science",
        "marks": 82
    }

    if student["marks"] >= 85:
        student["grade"] = "A"
    elif student["marks"] >= 70:
        student["grade"] = "B"
    else:
        student["grade"] = "C"

    print("\n--- Student Details ---")
    for key, value in student.items():
        print(f"{key}: {value}")

    ai_tools_set_1 = {"ChatGPT", "TensorFlow", "PyTorch"}
    ai_tools_set_2 = {"Scikit-learn", "TensorFlow", "Keras"}

    print("\nCommon AI Tools:", ai_tools_set_1.intersection(ai_tools_set_2))


# =====================================================
# Task 4: File Handling
# =====================================================

def file_handling():
    """Create, write, and read student data from file"""

    students = [
        ("Amit", 78, "B"),
        ("Sneha", 88, "A"),
        ("Rahul", 65, "C"),
        ("Pooja", 92, "A"),
        ("Neha", 74, "B")
    ]

    with open("ai_students.txt", "w") as file:
        for s in students:
            file.write(f"{s[0]},{s[1]},{s[2]}\n")

    print("\n--- Students with Marks Above 75 ---")
    with open("ai_students.txt", "r") as file:
        for line in file:
            name, marks, grade = line.strip().split(",")
            if int(marks) > 75:
                print(f"{name} - {marks} ({grade})")


# =====================================================
# Task 5: Mini Project – AI Prompt Logger
# =====================================================

from datetime import datetime

def prompt_logger():
    """Log AI prompts with timestamps"""

    prompt = input("\nEnter AI prompt: ").strip()

    if not prompt:
        print("Empty prompt not logged.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("prompt_history.txt", "a") as file:
        file.write(f"[{timestamp}] {prompt}\n")

    print("Prompt logged successfully.")


# =====================================================
# Main Execution
# =====================================================

if __name__ == "__main__":
    basic_operations()
    list_and_array_operations()
    dictionary_and_sets()
    file_handling()
    prompt_logger()

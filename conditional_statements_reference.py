"""
PYTHON CONDITIONAL STATEMENTS — COMPLETE REFERENCE
====================================================
Covers: if, if-else, if-elif-else, nested if, ternary operator,
match-case (Python 3.10+), logical operators, membership/identity
checks in conditions, and truthy/falsy conditions.
"""

# ----------------------------------------------------
# 1. Simple if
# ----------------------------------------------------
age = 20
if age >= 18:
    print("You are an adult.")


# ----------------------------------------------------
# 2. if-else
# ----------------------------------------------------
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# ----------------------------------------------------
# 3. if-elif-else (multiple conditions)
# ----------------------------------------------------
marks = 75
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)


# ----------------------------------------------------
# 4. Nested if
# ----------------------------------------------------
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")


# ----------------------------------------------------
# 5. Ternary (conditional expression)
# ----------------------------------------------------
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)


# ----------------------------------------------------
# 6. Logical operators in conditions (and / or / not)
# ----------------------------------------------------
age = 25
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today")

logged_in = False
if not logged_in:
    print("Please log in")


# ----------------------------------------------------
# 7. Membership operators (in / not in)
# ----------------------------------------------------
fruits = ["apple", "banana", "mango"]
item = "banana"
if item in fruits:
    print(f"{item} is available")
else:
    print(f"{item} is not available")


# ----------------------------------------------------
# 8. Identity operators (is / is not)
# ----------------------------------------------------
x = None
if x is None:
    print("x has no value")

y = 5
if y is not None:
    print("y has a value")


# ----------------------------------------------------
# 9. Chained comparisons
# ----------------------------------------------------
num = 50
if 10 <= num <= 100:
    print("num is between 10 and 100")


# ----------------------------------------------------
# 10. Truthy / Falsy conditions
#     (False, None, 0, 0.0, "", [], {}, () are all falsy)
# ----------------------------------------------------
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")

name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name not provided")


# ----------------------------------------------------
# 11. match-case (structural pattern matching, Python 3.10+)
# ----------------------------------------------------
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4 | 5:
        print("Thursday or Friday")
    case _:
        print("Weekend or invalid day")


# ----------------------------------------------------
# 12. match-case with pattern matching on data structures
# ----------------------------------------------------
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On the Y-axis at {y}")
    case (x, 0):
        print(f"On the X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Not a point")


# ----------------------------------------------------
# 13. Conditional with pandas (common real-world use case)
# ----------------------------------------------------
import pandas as pd

df = pd.DataFrame({"Salary": [5000, 12000, 25000, 45000]})

# Single condition
df["High_Earner"] = df["Salary"] > 20000

# Multiple conditions using apply + if-elif-else
def categorize(salary):
    if salary < 10000:
        return "Low"
    elif salary < 30000:
        return "Medium"
    else:
        return "High"

df["Category"] = df["Salary"].apply(categorize)

# Vectorized alternative using numpy.select (faster for large data)
import numpy as np
conditions = [
    df["Salary"] < 10000,
    df["Salary"] < 30000,
]
choices = ["Low", "Medium"]
df["Category_np"] = np.select(conditions, choices, default="High")

print(df)

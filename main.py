# main.py
# This file IMPORTS and USES the custom module 'calculator.py'
# Both files must be in the SAME folder.

# Method 1: import the whole module
import calculator

# Method 2: import specific items
from calculator import circle_area, Student

# Method 3: import with an alias
import calculator as calc


print("----- Method 1: import calculator -----")
print("Add:", calculator.add(10, 5))
print("Subtract:", calculator.subtract(10, 5))
print("Multiply:", calculator.multiply(10, 5))
print("Divide:", calculator.divide(10, 5))
print("Divide by zero:", calculator.divide(10, 0))
print("PI from module:", calculator.PI)
print("Author:", calculator.AUTHOR)

print("\n----- Method 2: from calculator import ... -----")
print("Circle area (r=5):", circle_area(5))

s1 = Student("Ravi", 85)
print(s1.display())

print("\n----- Method 3: import calculator as calc -----")
print("Add using alias:", calc.add(100, 200))

print("\n----- Inspecting the module -----")
print("Functions/variables in calculator:")
print([item for item in dir(calculator) if not item.startswith("__")])

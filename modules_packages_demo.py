# modules_packages_demo.py
# All-in-one file demonstrating Python Modules & Packages concepts
# (Normally these would be separate files/folders, combined here for convenience)

import math
import random
import datetime


# ---------- Simulating a custom module: mymodule.py ----------
pi_value = 3.14159

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def square(n):
    return n ** 2


# ---------- Simulating a package: mypackage/module1.py ----------
def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0


# ---------- Simulating a package: mypackage/module2.py ----------
def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()


# ---------- Main program ----------
def main():
    print("----- Built-in Modules -----")
    print("Square root of 16:", math.sqrt(16))
    print("Value of pi:", math.pi)
    print("Random number (1-10):", random.randint(1, 10))
    print("Current date & time:", datetime.datetime.now())

    print("\n----- Custom Module Functions -----")
    print(greet("Ravi"))
    print("Sum of 5 + 3:", add(5, 3))
    print("Square of 6:", square(6))
    print("Pi value:", pi_value)

    print("\n----- Custom Package Functions -----")
    print("6 x 7 =", multiply(6, 7))
    print("Is 10 even?", is_even(10))
    print("Reversed 'python':", reverse_string("python"))
    print("Uppercase 'hello':", to_uppercase("hello"))


if __name__ == "__main__":
    main()

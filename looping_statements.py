"""
ALL LOOPING STATEMENTS IN PYTHON
==================================
This file demonstrates every type of loop and loop-control
statement available in Python.
"""

# ---------------------------------------------------------
# 1. FOR LOOP - iterate over a sequence
# ---------------------------------------------------------
print("1. For loop (range):")
for i in range(5):
    print(i)

print("\n1b. For loop (list):")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n1c. For loop (string):")
for char in "Hi!":
    print(char)

print("\n1d. For loop (dictionary):")
person = {"name": "Alex", "age": 30}
for key, value in person.items():
    print(key, "->", value)


# ---------------------------------------------------------
# 2. WHILE LOOP - repeat while condition is true
# ---------------------------------------------------------
print("\n2. While loop:")
i = 0
while i < 5:
    print(i)
    i += 1


# ---------------------------------------------------------
# 3. DO-WHILE STYLE LOOP - Python has no native do-while,
#    simulate with while True + break
# ---------------------------------------------------------
print("\n3. Do-while style loop:")
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break


# ---------------------------------------------------------
# 4. NESTED LOOP - a loop inside another loop
# ---------------------------------------------------------
print("\n4. Nested loop:")
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")


# ---------------------------------------------------------
# 5. LOOP CONTROL STATEMENTS
# ---------------------------------------------------------
print("\n5a. Break:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n5b. Continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("\n5c. Else (runs only if loop completes without break):")
for i in range(5):
    print(i)
else:
    print("Loop finished without break")

print("\n5d. Pass (does nothing, acts as placeholder):")
for i in range(3):
    pass
print("Loop with pass completed")


# ---------------------------------------------------------
# 6. LIST COMPREHENSION - compact loop syntax
# ---------------------------------------------------------
print("\n6. List comprehension:")
squares = [x * x for x in range(5)]
print(squares)

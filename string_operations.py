"""
PYTHON STRING OPERATIONS — COMPLETE REFERENCE
Run this file to see every operation's output printed live.
"""

# ============================================================
# 1. CREATING STRINGS
# ============================================================
s1 = 'Hello World'
s2 = "Hello World"
s3 = '''Multi
line
string'''
s4 = str(123)          # from another type

print("1. CREATING STRINGS")
print(s1, s2, s3, s4, sep=" | ")
print()

# ============================================================
# 2. INDEXING & SLICING
# ============================================================
s = "Python Programming"

print("2. INDEXING & SLICING")
print("First char:", s[0])
print("Last char:", s[-1])
print("Slice [0:6]:", s[0:6])
print("Slice [7:]:", s[7:])
print("Reversed:", s[::-1])
print("Every 2nd char:", s[::2])
print()

# ============================================================
# 3. CONCATENATION & REPETITION
# ============================================================
a, b = "Hello", "World"

print("3. CONCATENATION & REPETITION")
print("Concat:", a + " " + b)
print("Repeat:", a * 3)
print()

# ============================================================
# 4. LENGTH & MEMBERSHIP
# ============================================================
print("4. LENGTH & MEMBERSHIP")
print("Length:", len(s))
print("'Pro' in s:", "Pro" in s)
print("'xyz' not in s:", "xyz" not in s)
print()

# ============================================================
# 5. CASE CONVERSION
# ============================================================
text = "Hello World"

print("5. CASE CONVERSION")
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())
print("swapcase():", text.swapcase())
print()

# ============================================================
# 6. WHITESPACE HANDLING
# ============================================================
padded = "   messy string   "

print("6. WHITESPACE HANDLING")
print("strip():", repr(padded.strip()))
print("lstrip():", repr(padded.lstrip()))
print("rstrip():", repr(padded.rstrip()))
print()

# ============================================================
# 7. SEARCHING
# ============================================================
sentence = "the quick brown fox jumps over the lazy dog"

print("7. SEARCHING")
print("find('fox'):", sentence.find("fox"))
print("find('cat') [not found -> -1]:", sentence.find("cat"))
print("rfind('the'):", sentence.rfind("the"))
print("index('quick'):", sentence.index("quick"))
print("count('the'):", sentence.count("the"))
print("startswith('the'):", sentence.startswith("the"))
print("endswith('dog'):", sentence.endswith("dog"))
print()

# ============================================================
# 8. SPLITTING & JOINING
# ============================================================
csv_line = "apple,banana,cherry"
words = "The quick brown fox"

print("8. SPLITTING & JOINING")
print("split(','):", csv_line.split(","))
print("split() [default whitespace]:", words.split())
print("splitlines():", "line1\nline2\nline3".splitlines())
print("join():", "-".join(["a", "b", "c"]))
print("partition(','):", csv_line.partition(","))
print()

# ============================================================
# 9. REPLACING
# ============================================================
msg = "I like cats. Cats are great."

print("9. REPLACING")
print("replace():", msg.replace("cats", "dogs"))
print("replace() with count:", msg.replace("Cats", "Dogs", 1))
print()

# ============================================================
# 10. CHECKING STRING TYPE / CONTENT
# ============================================================
print("10. CHECKING STRING TYPE")
print("'123'.isdigit():", "123".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())
print("'   '.isspace():", "   ".isspace())
print("'Hello'.isupper():", "Hello".isupper())
print("'HELLO'.isupper():", "HELLO".isupper())
print("'hello'.islower():", "hello".islower())
print("'Hello World'.istitle():", "Hello World".istitle())
print()

# ============================================================
# 11. FORMATTING STRINGS
# ============================================================
name, age = "Alice", 30

print("11. FORMATTING STRINGS")
print(f"f-string: {name} is {age} years old")
print("format(): {} is {} years old".format(name, age))
print("% operator: %s is %d years old" % (name, age))
print(f"Padding: |{name:>10}|{name:<10}|{name:^10}|")
print(f"Number format: {3.14159:.2f}")
print(f"With commas: {1000000:,}")
print()

# ============================================================
# 12. ALIGNMENT & PADDING
# ============================================================
word = "hi"

print("12. ALIGNMENT & PADDING")
print("center(10, '*'):", word.center(10, "*"))
print("ljust(10, '-'):", word.ljust(10, "-"))
print("rjust(10, '-'):", word.rjust(10, "-"))
print("zfill(5):", "42".zfill(5))
print()

# ============================================================
# 13. ENCODING / DECODING
# ============================================================
print("13. ENCODING / DECODING")
encoded = "hello".encode("utf-8")
print("encode():", encoded)
print("decode():", encoded.decode("utf-8"))
print()

# ============================================================
# 14. STRING COMPARISON
# ============================================================
print("14. STRING COMPARISON")
print("'apple' == 'apple':", "apple" == "apple")
print("'apple' < 'banana':", "apple" < "banana")
print()

# ============================================================
# 15. IMMUTABILITY DEMO
# ============================================================
print("15. IMMUTABILITY")
original = "hello"
modified = original.replace("h", "j")   # creates a NEW string
print("original:", original)
print("modified:", modified)
print()

# ============================================================
# 16. MISC USEFUL METHODS
# ============================================================
print("16. MISC USEFUL METHODS")
print("'Hello'.ljust(10) + '|':", "'" + "Hello".ljust(10) + "'")
print("maketrans + translate:",
      "hello".translate(str.maketrans("el", "ip")))
print("removeprefix (3.9+):", "unhappy".removeprefix("un"))
print("removesuffix (3.9+):", "filename.txt".removesuffix(".txt"))

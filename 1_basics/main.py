"""
Phase 0: Basic Syntax & Data Types in Python
==============================================
Senior SRE Tip: Python e dynamic typing thaklew type clarity bojha prod issue avoid korte shahajjo kore.
"""

# ---------------------------------------------------------
# 1. Variables & Dynamic Typing
# ---------------------------------------------------------
# Python dynamic language. Explicitly variable type define korte hoy na.
user_name = "Awolad"       # str
user_age = 25              # int
is_active = True           # bool
hourly_rate = 45.50        # float

print("--- 1. Variables & Dynamic Typing ---")
print(f"Name: {user_name}, Type: {type(user_name)}")
print(f"Age: {user_age}, Type: {type(user_age)}")
print(f"Is Active: {is_active}, Type: {type(is_active)}")
print(f"Hourly Rate: {hourly_rate}, Type: {type(hourly_rate)}")
print()

# Dynamic Re-assignment
data = 100
print(f"Initial data: {data} ({type(data)})")
data = "Now I am a string"
print(f"Re-assigned data: {data} ({type(data)})\n")


# ---------------------------------------------------------
# 2. String Formatting (f-strings & String Methods)
# ---------------------------------------------------------
# f-strings (Formatted String Literals) - Modern & Fast
service_name = "  fastapi-auth-service  "
port = 8000

print("--- 2. String Formatting & Methods ---")
cleaned_service_name = service_name.strip()
uppercase_service = cleaned_service_name.upper()

print(f"Original: '{service_name}'")
print(f"Cleaned & Uppercase: '{uppercase_service}'")
print(f"Server starting: http://localhost:{port}/healthz\n")


# ---------------------------------------------------------
# 3. Type Conversion (Type Casting)
# ---------------------------------------------------------
print("--- 3. Type Casting ---")
str_num = "150"
int_num = int(str_num)      # String to Int
float_num = float(int_num)  # Int to Float

print(f"String '{str_num}' -> Int {int_num} ({type(int_num)}) -> Float {float_num} ({type(float_num)})")

# Boolean Casting Examples
print(f"bool('') -> {bool('')}")        # Empty string is False
print(f"bool('hello') -> {bool('hello')}") # Non-empty string is True
print(f"bool(0) -> {bool(0)}")          # 0 is False
print(f"bool(42) -> {bool(42)}")        # Non-zero integer is True

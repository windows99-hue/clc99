"""
Demo script for loading99 decorator functionality
展示 loading99 装饰器所有功能的演示脚本
"""

import time
import sys
import os
from clc99 import loading99, err99, FAILEDException

# Demo 1: Basic usage with default settings
print("1. Basic Usage with Default Settings")
@loading99()
def basic_function():
    """A simple function that runs successfully"""
    time.sleep(0.5)
    return "Basic result"

result = basic_function()
print(f"Result: {result}")
print()

# Demo 2: Custom loading and success text
print("2. Custom Loading and Success Text")
@loading99(text="Processing data...", success_text="COMPLETED")
def data_processing():
    """Function with custom text"""
    time.sleep(0.3)
    return "Data processed"

data_processing()
print()

# Demo 3: Show internal prints (suppress_output=False)
print("3. Show Internal Print Output")
@loading99(text="Debug mode...", success_text="DEBUG_DONE", suppress_output=False)
def debug_function():
    """Function that shows internal prints"""
    print("  Internal debug message 1")
    time.sleep(0.2)
    print("  Internal debug message 2")
    return "Debug completed"

debug_function()
print()

# Demo 4: Hide success text
print("4. Hide Success Text")
@loading99(text="Silent operation...", output_success_text=False)
def silent_function():
    """Function that doesn't show success text"""
    time.sleep(0.3)
    return "Silent result"

silent_function()
print("  (Success text was hidden)")
print()

# Demo 5: Using err99() to interrupt execution
print("5. Using err99() to Interrupt Execution")
@loading99(text="User validation...", success_text="VALID")
def user_validation(age):
    """Function that can be interrupted by err99()"""
    if age < 18:
        err99("User must be at least 18 years old")
        return
    
    if age > 100:
        err99("INVALID_AGE", "Age seems unrealistic")
        return
        
    time.sleep(0.3)
    return f"User age {age} is valid"

print("Testing with age 16:")
user_validation(16)
print()

print("Testing with age 25:")
result = user_validation(25)
print(f"Result: {result}")
print()

print("Testing with age 150:")
user_validation(150)
print()

# Demo 6: Exception handling
print("6. Exception Handling")
@loading99(text="Risky operation...", except_text="ERROR")
def risky_operation(should_fail=False):
    """Function that might raise exceptions"""
    if should_fail:
        raise ValueError("Something went wrong!")
    time.sleep(0.3)
    return "Operation successful"

print("Testing normal execution:")
risky_operation(should_fail=False)
print()

print("Testing with exception:")
try:
    risky_operation(should_fail=True)
except Exception as e:
    print(f"  Exception caught: {e}")
print()

# Demo 7: Function with automatic name detection
print("7. Automatic Function Name Detection")
@loading99()  # No text provided, uses function name
def calculate_statistics():
    """Function that uses automatic naming"""
    time.sleep(0.4)
    return "Statistics calculated"

calculate_statistics()
print()

# Demo 8: Combination of features
print("8. Combined Features Demo")
@loading99(
    text="Comprehensive task...", 
    success_text="ALL_DONE", 
    suppress_output=True,
    output_success_text=True
)
def comprehensive_task():
    """Function combining multiple features"""
    print("This won't be displayed due to suppress_output")
    time.sleep(0.3)
    
    # Some conditional logic
    import random
    if random.random() < 0.3:
        err99("RANDOM_FAIL", "Random failure condition met")
        return
        
    return "Task completed successfully"

print("Running comprehensive task (may randomly fail):")
for i in range(3):
    result = comprehensive_task()
    if result:
        print(f"  Attempt {i+1}: {result}")
    else:
        print(f"  Attempt {i+1}: Failed")
print()

# Demo 9: Real-world example - file processing
print("9. Real-world Example - File Processing")

def file_exists(filename):
    return os.path.exists(filename)

def has_read_permission(filename):
    return os.access(filename, os.R_OK)

@loading99(text="Processing file...", success_text="FILE_PROCESSED")
def process_file(filename):
    """Real-world file processing with validation"""
    if not file_exists(filename):
        err99(text=f"File '{filename}' not found",error_text="FILE_MISSING")
        return
        
    if not has_read_permission(filename):
        err99(error_text="PERMISSION_DENIED", text=f"No read permission for '{filename}'")
        return
        
    # Simulate file processing
    time.sleep(0.5)
    return f"Processed {filename}"

print("Testing with non-existent file:")
process_file("nonexistent.txt")
print()

print("Testing with current file (should work):")
result = process_file(__file__)  # Process this demo file itself
if result:
    print(f"  {result}")
print()

print("=== Demo Completed ===")
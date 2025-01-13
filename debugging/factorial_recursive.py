#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a non-negative integer n.
# It uses recursion to compute the factorial by multiplying n with the factorial of (n-1).
# The base case is when n is 0, where the factorial is defined as 1.

# Parameters:
# n (int): The non-negative integer for which the factorial will be computed.

# Returns:
# int: The factorial of the input integer n.

def factorial(n):
    # Base case: If n is 0, return 1 (0! = 1)
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial(n-1)
        return n * factorial(n-1)

# Get the input number from the command-line arguments and convert it to an integer.
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation.
print(f)

# Python Average Calculation with Exception Handling

This repository demonstrates a common error in Python code: failure to handle exceptions, specifically in the case of calculating the average of an empty list. The original code leads to a `ZeroDivisionError`. The solution provides improved exception handling to gracefully deal with this scenario.

## Bug Report

The `calculate_average` function crashes if it receives an empty list as input because it attempts to divide by zero. This can be improved by incorporating error handling. 

## Solution

The solution includes a check for an empty list and returns 0 in that case.  This prevents the program from crashing.  This is a more robust and user-friendly approach.
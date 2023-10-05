Project Title: Arithmetic Arranger

The Arithmetic Arranger project aims to develop a Python function that receives a list of arithmetic problems and arranges them vertically, following specific formatting rules. The function provides a helpful tool for students, particularly in primary school, to visually organize arithmetic problems and their solutions.

The key features and rules of the Arithmetic Arranger function are as follows:

Vertical Arrangement: The function arranges the arithmetic problems vertically, similar to how students commonly write them in primary school.
Right Alignment: Numbers within the problems are right-aligned to maintain a neat and organized layout.
Operator Placement: The operator is placed on the same line as the second operand, aligned with the rightmost digit of the first operand.
Proper Spacing: Four spaces separate each problem to ensure clear differentiation.
Bottom Dashes: A line of dashes is displayed beneath each problem, covering the entire length of the problem individually.
Error Handling: The function includes error handling for various scenarios, such as exceeding the maximum number of problems, using invalid operators, including non-digit characters in numbers, and exceeding the maximum width of four digits for operands.
The project consists of the following main components:

arithmetic_arranger.py: This module contains the arithmetic_arranger function, which accepts a list of arithmetic problems as input and returns the arranged problems as a formatted string. It handles the logic for organizing the problems and implementing error checks based on the specified rules.
main.py: This file allows users to test the arithmetic_arranger function by providing different arithmetic problem sets and viewing the output.
test_module.py: This module contains unit tests for the arithmetic_arranger function. It verifies the correctness of the function's implementation by comparing the actual output with the expected output for various test cases.
By executing main.py or running the unit tests using test_module.py, users can ensure the proper functionality of the arithmetic_arranger function and confirm that it follows the required rules for formatting arithmetic problems vertically.

The Arithmetic Arranger project serves as an educational tool for students and demonstrates the ability to implement logical operations, string manipulation, and error handling in Python.





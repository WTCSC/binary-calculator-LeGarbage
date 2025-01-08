[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17649988)
# Binary Calculator

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
- The solution must be implemented as a function called `binary_calculator()` with three parameters:
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function.
- Implement your own binary-to-decimal and decimal-to-binary conversion logic.
- All binary inputs and outputs should be strings.
- Handle division by zero by returning `"NaN"`
- Handle decimal numbers by rounding down to the nearest whole number (flooring).
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->

There are 2 types of people in this world: people who need to do mathematical operations with binary numbers, and normal people. If you find yourself to be of the former, then this binary calculator is for you! This calculator is incredibly sophisticated, being able to perform addition, subtraction, multiplication, and even division.

## How to use
 
- Download calculator.py and import it into your project
- Call the *binary_calculator* function, which takes 3 arguments
    - *bin1* [str] The first binary number you want to operate on (either the addend, subtrahend, factor, or dividend in addition, subtraction, multiplication, or division respectively)
    - *bin2* [str] The second binary number you want to operate on (either the addend, minuend, factor, or divisor in addition, subtraction, multiplication, or division respectively)
    - *operator* [str] The operation to perform (can be +, -, *, or /)
- The *binary_calculator* returns the result of the operation as a binary number in a string

## Features

- Returns NaN for division by zero
- Returns Error for non-binary numbers or invalid characters
- Returns Overflow for negative results or results larger than 8 bits (over 255)
# 0x00-pascal_triangle

## Overview
This Python project implements a Pascal's Triangle generator. Pascal's Triangle is a mathematical structure that demonstrates several interesting properties and relationships, including binomial coefficients and the Fibonacci sequence.

The main functionality of this project is encapsulated in the `pascal_triangle` function, which takes an integer n as input and returns a list of lists representing the first n rows of Pascal's Triangle.

Additionally, the project includes unit tests to ensure the correctness of the `pascal_triangle` function.

## Features
- Generate Pascal's Triangle up to a specified number of rows.
- Validate input to ensure it is a positive integer.
- Handle invalid input gracefully by raising a ValueError.
- Unit tests to verify the correctness of the implementation.

## Requirements
To run the Pascal's Triangle generator, you need:

- Python 3.x installed on your system.

## Usage
To use the Pascal's Triangle generator:

1. Import the `pascal_triangle` function from the `pascal_triangle` module.
2. Call the `pascal_triangle` function with the desired number of rows as an argument.
3. The function will return a list of lists representing Pascal's Triangle up to the specified number of rows.
Example usage:
```
from pascal_triangle import pascal_triangle

# Generate Pascal's Triangle with 5 rows
triangle = pascal_triangle(5)
print(triangle)
```


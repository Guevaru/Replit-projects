# Polygon Area Calculator

This Python project implements a Polygon Area Calculator using object-oriented programming. It includes two classes: `Rectangle` and `Square`. The `Square` class is a subclass of `Rectangle` and inherits its methods and attributes.

The Polygon Area Calculator provides the following functionalities:

- Calculating the area, perimeter, and diagonal of a rectangle
- Generating a visual representation of the rectangle using asterisks (`*`)
- Determining the number of times a given shape can fit inside a rectangle
## Installation

1. Clone the repository to your local machine.
2. Open the project in your preferred Python environment.

## Usage

To use the Polygon Area Calculator, follow these steps:

1. Import the required classes from `shape_calculator.py`:
    ```python
    from shape_calculator import Rectangle, Square
    ```

2. Create instances of the `Rectangle` and `Square` classes, specifying the required dimensions:
    ```python
    rect = Rectangle(10, 5)
    sq = Square(9)
    ```

3. Utilize the available methods to perform calculations and retrieve information:
    ```python
    # Example with a rectangle
    print(rect.get_area())  # Output: 50
    rect.set_height(3)
    print(rect.get_perimeter())  # Output: 26
    print(rect)  # Output: Rectangle(width=10, height=3)
    print(rect.get_picture())
    """
    **********
    **********
    **********
    """

    # Example with a square
    print(sq.get_area())  # Output: 81
    sq.set_side(4)
    print(sq.get_diagonal())  # Output: 5.656854249492381
    print(sq)  # Output: Square(side=4)
    print(sq.get_picture())
    """
    ****
    ****
    ****
    ****
    """

    # Example of fitting a shape inside the rectangle
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))  # Output: 8
    ```

4. Run `main.py` to execute the provided usage examples and see the results.

## Testing

The project includes unit tests in `test_module.py` to ensure the correctness of the implemented classes and methods. To run the tests, execute the following command:


The test results will be displayed, indicating whether all the tests have passed successfully or if there are any failures that require attention.


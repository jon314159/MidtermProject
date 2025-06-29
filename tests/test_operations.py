import pytest
from app.operations import operations

def test_addition_positive():
    """
    Test addition of two positive numbers.
    """
    a = 5
    b = 3
    assert operations.add(a, b) == 8, "Addition failed"

def test_addition_negative():
    """
    Test addition of two negative numbers.
    """
    a = -5
    b = -3
    assert operations.add(a, b) == -8, "Addition failed"

def test_subtraction_positive():
    """
    Test subtraction where both operands are positive.
    """
    a = 5
    b = 3
    assert operations.subtract(a, b) == 2, "Subtraction failed"

def test_subtraction_negative():
    """
    Test subtraction where both operands are negative.
    """
    a = -5
    b = -3
    assert operations.subtract(a, b) == -2, "Subtraction failed"

def test_division_positive():
    """
    Test division of two positive numbers.
    """
    a = 6
    b = 3
    assert operations.divide(a, b) == 2, "Division failed"

def test_division_by_zero():
    """
    Test division by zero and expect ValueError.

    :raises ValueError: If b is 0.
    """
    a = 6
    b = 0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        operations.divide(a, b)

def test_multiplication_positive():
    """
    Test multiplication of two positive numbers.
    """
    a = 5
    b = 3
    assert operations.multiply(a, b) == 15, "Multiplication failed"

def test_multiplication_negative():
    """
    Test multiplication of two negative numbers.
    """
    a = -5
    b = -3
    assert operations.multiply(a, b) == 15, "Multiplication failed"

def test_power_positive():
    """
    Test exponentiation with positive base and exponent.
    """
    a = 2
    b = 3
    assert operations.power(a, b) == 8, "Power operation failed"

def test_power_negative():
    """
    Test exponentiation with negative base and positive exponent.
    """
    a = -2
    b = 3
    assert operations.power(a, b) == -8, "Power operation failed"

def test_modulus_positive():
    """
    Test modulus operation with positive operands.
    """
    a = 5
    b = 3
    assert operations.modulus(a, b) == 2, "Modulus operation failed"

def test_modulus_negative():
    """
    Test modulus operation with negative operands.
    """
    a = -5
    b = -3
    assert operations.modulus(a, b) == -2, "Modulus operation failed"

def test_percentage_positive():
    """
    Test calculating percentage a of b.
    """
    a = 50
    b = 200
    assert operations.percentage(a, b) == 25.0, "Percentage operation failed"

def test_percentage_zero_divisor():
    """
    Test percentage operation when b is 0.
    """
    a = 50
    b = 0
    assert operations.percentage(a, b) == 0, "Percentage operation with zero divisor failed"

def test_absolute_difference_positive():
    """
    Test absolute difference with positive values.
    """
    a = 10
    b = 5
    assert operations.absolute_difference(a, b) == 5, "Absolute difference failed"

def test_absolute_difference_negative():
    """
    Test absolute difference with negative values.
    """
    a = -10
    b = -5
    assert operations.absolute_difference(a, b) == 5, "Absolute difference failed"

def test_square_root_positive():
    """
    Test square root of a positive number.
    """
    a = 16
    assert operations.square_root(a) == 4, "Square root operation failed"

def test_integer_division_positive():
    """
    Test integer division of two positive integers.
    """
    a = 5
    b = 2
    assert operations.integer_division(a, b) == 2, "Integer division failed"

def test_integer_division_negative():
    """
    Test integer division of two negative integers.
    """
    a = -5
    b = -2
    assert operations.integer_division(a, b) == 2, "Integer division failed"

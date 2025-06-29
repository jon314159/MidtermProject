import pytest
from app.operations import operations

def test_addition_positive():
    a = 5
    b = 3
    assert operations.add(a, b) == 8, "Addition failed"

def test_addition_negative():
    a = -5
    b = -3
    assert operations.add(a, b) == -8, "Addition failed"

def test_subtraction_positive():
    a = 5
    b = 3
    assert operations.subtract(a, b) == 2, "Subtraction failed"
def test_subtraction_negative():
    a = -5
    b = -3
    assert operations.subtract(a, b) == -2, "Subtraction failed"

def test_division_positive():
    a = 6
    b = 3
    assert operations.divide(a, b) == 2, "Division failed"

def test_division_by_zero():
    a = 6
    b = 0

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        assert operations.divide(a, b) == float('inf'), "Division by zero did not raise ValueError"

def test_multiplication_positive():
    a = 5
    b = 3
    assert operations.multiply(a, b) == 15, "Multiplication failed"

def test_multiplication_negative():
    a = -5
    b = -3
    assert operations.multiply(a, b) == 15, "Multiplication failed"

def test_power_positive():
    a = 2
    b = 3
    assert operations.power(a, b) == 8, "Power operation failed"


def test_power_negative():
    a = -2
    b = 3
    assert operations.power(a, b) == -8, "Power operation failed"
    

def test_modulus_positive():
    a = 5
    b = 3
    assert operations.modulus(a, b) == 2, "Modulus operation failed"

def test_modulus_negative():
    a = -5
    b = -3
    assert operations.modulus(a, b) == -2, "Modulus operation failed"
    

def test_percentage_positive():
    a = 50
    b = 200
    assert operations.percentage(a, b) == 25.0, "Percentage operation failed"

def test_percentage_zero_divisor():
    a = 50
    b = 0
    assert operations.percentage(a, b) == 0, "Percentage operation with zero divisor failed"

def test_absolute_difference_positive():
    a = 10
    b = 5
    assert operations.absolute_difference(a, b) == 5, "Absolute difference failed"
    

def test_absolute_difference_negative():
    a = -10
    b = -5
    assert operations.absolute_difference(a, b) == 5, "Absolute difference failed"

def test_square_root_positive():
    a = 16
    assert operations.square_root(a) == 4, "Square root operation failed"

def integar_division_positive():
    a = 5
    b = 2
    assert operations.integer_division(a, b) == 2, "Integer division failed"

def integer_division_negative():
    a = -5
    b = -2
    assert operations.integer_division(a, b) == 2, "Integer division failed"


import pytest
from app.calculation import CalculationFactory

def test_create_calculation_not_registered():
    """
    Ensure create_calculation raises ValueError if the calculation is not registered.
    """
    with pytest.raises(ValueError, match="Calculation unknown_op is not registered."):
        CalculationFactory.create_calculation("unknown_op", 1.0, 2.0)

@pytest.mark.parametrize("name, a, b, expected", [
    ("add", 5, 3, 8),
    ("subtract", 5, 3, 2),
    ("multiply", 5, 3, 15),
    ("divide", 6, 3, 2),
    ("power", 2, 3, 8),
    ("modulus", 5, 3, 2),
    ("percentage", 50, 200, 25.0),
    ("absolute_difference", 10, 5, 5),
    ("integer_division", 5, 2, 2),
])
def test_binary_operations(name, a, b, expected):
    calc = CalculationFactory.create_calculation(name, a, b)
    result = calc.execute()
    assert result == expected
    assert calc.result == expected


def test_square_root_operation():
    calc = CalculationFactory.create_calculation("square_root", 16, 0)  # b ignored
    result = calc.execute()
    assert result == 4
    assert calc.result == 4


def test_divide_by_zero():
    calc = CalculationFactory.create_calculation("divide", 5, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.execute()


def test_square_root_negative():
    calc = CalculationFactory.create_calculation("square_root", -9, 0)
    with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
        calc.execute()


def test_integer_division_by_zero():
    calc = CalculationFactory.create_calculation("integer_division", 5, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.execute()


def test_unregistered_calculation():
    with pytest.raises(ValueError, match="Calculation fake_op is not registered."):
        CalculationFactory.create_calculation("fake_op", 1, 1)

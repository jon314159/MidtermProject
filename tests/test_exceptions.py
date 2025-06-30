import pytest
from app.exceptions import (
    CalculatorError,
    ValidationError,
    OperationError,
    FileProcessingError
)


def test_calculator_error_base():
    """
    Test that CalculatorError behaves like a standard exception.
    """
    with pytest.raises(CalculatorError) as exc:
        raise CalculatorError("Calculator base error")
    assert str(exc.value) == "Calculator base error"


def test_validation_error_is_subclass():
    """
    Test that ValidationError is a subclass of CalculatorError and raises correctly.
    """
    with pytest.raises(ValidationError) as exc:
        raise ValidationError("Invalid input value")
    assert isinstance(exc.value, CalculatorError)
    assert str(exc.value) == "Invalid input value"


def test_operation_error_is_subclass():
    """
    Test that OperationError is a subclass of CalculatorError and raises correctly.
    """
    with pytest.raises(OperationError) as exc:
        raise OperationError("Operation failed")
    assert isinstance(exc.value, CalculatorError)
    assert str(exc.value) == "Operation failed"


def test_file_processing_error_is_subclass():
    """
    Test that FileProcessingError is a subclass of CalculatorError and raises correctly.
    """
    with pytest.raises(FileProcessingError) as exc:
        raise FileProcessingError("Failed to read/write file")
    assert isinstance(exc.value, CalculatorError)
    assert str(exc.value) == "Failed to read/write file"

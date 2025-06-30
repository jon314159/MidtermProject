class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    pass


class ValidationError(CalculatorError):
    """Raised for invalid user input."""
    pass


class OperationError(CalculatorError):
    """Raised when an operation fails."""
    pass


class FileProcessingError(CalculatorError):
    """Raised when a data file fails to read/write."""
    pass

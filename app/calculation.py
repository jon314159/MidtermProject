from abc import abstractmethod
from app.operations import operations
from typing import Optional


class Calculation:
    """
    Abstract base class for all calculator operations.

    :param a: The first operand.
    :type a: float
    :param b: The second operand.
    :type b: float
    """

    def __init__(self, a: float, b: float):
        self.a: float = a #pragma: no cover
        self.b: float = b #pragma: no cover
        self.result: Optional[float] = None

    @abstractmethod
    def execute(self) -> float:
        """
        Execute the calculation. Must be implemented by subclasses.

        :return: The result of the operation.
        :rtype: float
        """
        pass #pragma: no cover

    def string(self) -> str:
        """
        Return a string representation of the calculation.

        :return: A formatted string with the class name and operands.
        :rtype: str
        """
        return f"{self.__class__.__name__}({self.a}, {self.b})" #pragma: no cover


class CalculationFactory:
    """
    Factory class to register and create calculation objects.
    """

    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_class):
        """
        Register a new calculation class in the factory.

        :param calculation_class: The class to register.
        :type calculation_class: type

        :return: A decorator that ensures the class is registered only once.
        :rtype: function
        """

        cls._calculations[calculation_class.__name__] = calculation_class #pragma: no cover

        def decorator(cls): #pragma: no cover
            cls.register_calculation(cls)
            if cls.__name__ not in cls._calculations:
                cls._calculations[cls.__name__] = cls
    @classmethod
    def create_calculation(cls, calculation_name: str, a: float, b: float) -> Calculation:
        """
        Create a registered calculation instance.

        :param calculation_name: Name of the registered class.
        :param a: First operand.
        :param b: Second operand.
        :return: Instance of a subclass of calculation.
        :raises ValueError: If calculation_name is not registered.
        """
        if calculation_name not in cls._calculations:
            raise ValueError(f"Calculation {calculation_name} is not registered.")
        return cls._calculations[calculation_name](a, b)